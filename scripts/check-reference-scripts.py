#!/usr/bin/env python3
"""Smoke-test public reference scripts against synthetic fixtures."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


evidence = load_module(
    "reference_evidence_payloads", ROOT / "reference-scripts" / "evidence_payloads.py"
)
templates = load_module("reference_templates", ROOT / "reference-scripts" / "templates.py")


def main() -> int:
    errors: list[str] = []
    _validate_fixtures(errors)
    _compare_template_outputs(errors)

    if errors:
        print("\n".join(errors))
        return 1

    print("reference scripts OK")
    return 0


def _validate_fixtures(errors: list[str]) -> None:
    candidate_paths = [
        ROOT / "fixtures" / "evidence" / "example-match-candidate.json",
        ROOT / "fixtures" / "templates" / "match-bridge-candidate.json",
        ROOT / "fixtures" / "templates" / "relationship-constrained-candidate.json",
    ]
    for path in candidate_paths:
        payload = evidence.load_json(path)
        errors.extend(_prefix(path, evidence.validate_candidate(payload)))

    for path in (
        ROOT / "fixtures" / "templates" / "split-season-stage-candidates.json",
    ):
        payload = evidence.load_json(path)
        if not isinstance(payload, list):
            errors.append(f"{path}: expected list payload")
            continue
        for index, item in enumerate(payload):
            errors.extend(
                _prefix(path, evidence.validate_candidate(item), suffix=f"[{index}]")
            )

    residue_paths = [
        ROOT / "fixtures" / "evidence" / "review-residue.json",
        ROOT / "fixtures" / "templates" / "candidate-recovery-residue.json",
    ]
    for path in residue_paths:
        payload = evidence.load_json(path)
        errors.extend(_prefix(path, evidence.validate_review_residue(payload)))

    errors.extend(
        _prefix(
            ROOT / "fixtures" / "evidence" / "source-constraints.json",
            evidence.validate_source_constraints(
                evidence.load_json(ROOT / "fixtures" / "evidence" / "source-constraints.json")
            ),
        )
    )


def _compare_template_outputs(errors: list[str]) -> None:
    expected_match = evidence.load_json(
        ROOT / "fixtures" / "templates" / "match-bridge-candidate.json"
    )
    actual_match = templates.match_bridge_candidate(
        provider="example_feed",
        external_id="match-001",
        match_label="Northbridge City v Eastport United",
        fixture_date="2026-05-10",
        home_external_id="team-home",
        away_external_id="team-away",
        competition_external_id="competition-001",
        season_external_id="season-2026",
        score=0.95,
    )
    _assert_equal(errors, "match_bridge_candidate", expected_match, actual_match)

    expected_relationship = evidence.load_json(
        ROOT / "fixtures" / "templates" / "relationship-constrained-candidate.json"
    )
    actual_relationship = templates.relationship_constrained_candidate(
        provider="example_feed",
        entity_type="player",
        external_id="player-001",
        target_label="A. Example",
        score=0.91,
        identity_evidence=[
            {
                "provider": "example_feed",
                "kind": "attribute",
                "entity_type": "player",
                "external_id": "player-001",
                "value": {
                    "name": "Alex Example",
                    "date_of_birth": "2001-02-03",
                },
                "source_role": "corroborator",
                "method": "attribute-corroboration",
                "confidence": 0.91,
            }
        ],
        relationships=[
            {
                "provider": "example_feed",
                "relationship_type": "appeared_for_team",
                "subject_external_id": "player-001",
                "object_external_id": "team-home",
                "subject_type": "player",
                "object_type": "team",
                "evidence_count": 3,
                "method": "lineup-overlap",
                "confidence": 0.9,
            }
        ],
        metadata={"template": "relationship-constrained-bridge"},
    )
    _assert_equal(
        errors,
        "relationship_constrained_candidate",
        expected_relationship,
        actual_relationship,
    )

    expected_split = evidence.load_json(
        ROOT / "fixtures" / "templates" / "split-season-stage-candidates.json"
    )
    actual_split = templates.split_season_stage_candidates(
        provider="example_feed",
        competition_external_id="league-001",
        season_external_id="season-2026",
        season_label="2026",
        stages={"stage-regular": "Regular season"},
    )
    _assert_equal(errors, "split_season_stage_candidates", expected_split, actual_split)

    expected_residue = evidence.load_json(
        ROOT / "fixtures" / "templates" / "candidate-recovery-residue.json"
    )
    actual_residue = templates.candidate_recovery_residue(
        provider="example_feed",
        entity_type="player",
        external_id="player-ambiguous",
        reason="two target players share the same date of birth and display name",
        candidate_ids=["candidate-a", "candidate-b"],
        next_action="request relationship evidence from lineups",
    )
    _assert_equal(errors, "candidate_recovery_residue", expected_residue, actual_residue)


def _assert_equal(errors: list[str], label: str, expected: Any, actual: Any) -> None:
    if evidence.stable_json(expected) != evidence.stable_json(actual):
        errors.append(f"{label}: generated payload does not match fixture")


def _prefix(path: Path, messages: list[str], *, suffix: str = "") -> list[str]:
    return [f"{path.relative_to(ROOT)}{suffix}: {message}" for message in messages]


if __name__ == "__main__":
    sys.exit(main())
