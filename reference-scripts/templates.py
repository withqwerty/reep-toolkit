#!/usr/bin/env python3
"""Non-mutating template builders for portable identity-resolution payloads.

These helpers emit dictionaries that match the JSON fixtures under ``fixtures/``.
They deliberately do not allocate target IDs, call provider APIs, or write to a
register. Treat them as copy-paste starting points for your own workflow.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any


def match_bridge_candidate(
    *,
    provider: str,
    external_id: str,
    match_label: str | None = None,
    fixture_date: str | None = None,
    home_external_id: str | None = None,
    away_external_id: str | None = None,
    competition_external_id: str | None = None,
    season_external_id: str | None = None,
    target_id: str | None = None,
    score: float | None = None,
    snapshot: str | None = None,
    method: str = "match-bridge-template",
    metadata: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a match candidate from one provider match ID plus fixture context."""

    evidence = [
        _drop_empty(
            {
                "provider": provider,
                "kind": "bridge",
                "entity_type": "match",
                "external_id": external_id,
                "target_id": target_id,
                "source_role": "bridge",
                "method": method,
                "confidence": score,
                "snapshot": snapshot,
            }
        )
    ]

    fixture_tuple = _drop_empty(
        {
            "date": fixture_date,
            "home_external_id": home_external_id,
            "away_external_id": away_external_id,
            "competition_external_id": competition_external_id,
            "season_external_id": season_external_id,
        }
    )
    if fixture_tuple:
        evidence.append(
            _drop_empty(
                {
                    "provider": provider,
                    "kind": "fixture_tuple",
                    "entity_type": "match",
                    "external_id": external_id,
                    "value": fixture_tuple,
                    "source_role": "corroborator",
                    "method": method,
                    "confidence": score,
                    "snapshot": snapshot,
                }
            )
        )

    relationships = [
        _relationship(
            provider,
            "home_team",
            external_id,
            home_external_id,
            "match",
            "team",
            method,
            score,
            snapshot,
        ),
        _relationship(
            provider,
            "away_team",
            external_id,
            away_external_id,
            "match",
            "team",
            method,
            score,
            snapshot,
        ),
        _relationship(
            provider,
            "competition",
            external_id,
            competition_external_id,
            "match",
            "competition",
            method,
            score,
            snapshot,
        ),
        _relationship(
            provider,
            "season",
            external_id,
            season_external_id,
            "match",
            "season",
            method,
            score,
            snapshot,
        ),
    ]

    return _drop_empty(
        {
            "candidate_id": f"{provider}:match:{external_id}",
            "entity_type": "match",
            "provider": provider,
            "external_id": external_id,
            "target_id": target_id,
            "target_label": match_label,
            "score": score,
            "method": method,
            "status": _target_status(target_id, score),
            "evidence": evidence,
            "relationship_evidence": [item for item in relationships if item],
            "blockers": [],
            "metadata": dict(metadata or {}),
        }
    )


def relationship_constrained_candidate(
    *,
    provider: str,
    entity_type: str,
    external_id: str,
    relationships: list[dict[str, Any]],
    identity_evidence: list[dict[str, Any]] | None = None,
    target_id: str | None = None,
    target_label: str | None = None,
    score: float | None = None,
    method: str = "relationship-constrained-template",
    blockers: list[dict[str, Any]] | None = None,
    metadata: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Package identity evidence plus relationship evidence into one candidate."""

    return _drop_empty(
        {
            "candidate_id": f"{provider}:{entity_type}:{external_id}",
            "entity_type": entity_type,
            "provider": provider,
            "external_id": external_id,
            "target_id": target_id,
            "target_label": target_label,
            "score": score,
            "method": method,
            "status": "accepted" if target_id and score == 1.0 else "review",
            "evidence": list(identity_evidence or ()),
            "relationship_evidence": list(relationships),
            "blockers": list(blockers or ()),
            "metadata": dict(metadata or {}),
        }
    )


def split_season_stage_candidates(
    *,
    provider: str,
    competition_external_id: str,
    season_external_id: str,
    season_label: str,
    stages: Mapping[str, str],
    target_season_id: str | None = None,
    snapshot: str | None = None,
    method: str = "split-season-stage-template",
) -> list[dict[str, Any]]:
    """Emit a parent-season candidate plus stage candidates for split seasons."""

    season = _drop_empty(
        {
            "candidate_id": f"{provider}:season:{season_external_id}",
            "entity_type": "season",
            "provider": provider,
            "external_id": season_external_id,
            "target_id": target_season_id,
            "target_label": season_label,
            "method": method,
            "status": "review",
            "evidence": [
                _drop_empty(
                    {
                        "provider": provider,
                        "kind": "bridge",
                        "entity_type": "season",
                        "external_id": season_external_id,
                        "target_id": target_season_id,
                        "source_role": "bridge",
                        "method": method,
                        "snapshot": snapshot,
                    }
                )
            ],
            "relationship_evidence": [
                _relationship(
                    provider,
                    "competition",
                    season_external_id,
                    competition_external_id,
                    "season",
                    "competition",
                    method,
                    None,
                    snapshot,
                )
            ],
            "blockers": [],
            "metadata": {},
        }
    )

    stage_candidates = [
        _drop_empty(
            {
                "candidate_id": f"{provider}:stage:{stage_external_id}",
                "entity_type": "stage",
                "provider": provider,
                "external_id": stage_external_id,
                "target_label": stage_label,
                "method": method,
                "status": "review",
                "evidence": [
                    _drop_empty(
                        {
                            "provider": provider,
                            "kind": "name",
                            "entity_type": "stage",
                            "external_id": stage_external_id,
                            "value": stage_label,
                            "source_role": "corroborator",
                            "method": method,
                            "snapshot": snapshot,
                        }
                    )
                ],
                "relationship_evidence": [
                    _relationship(
                        provider,
                        "season",
                        stage_external_id,
                        season_external_id,
                        "stage",
                        "season",
                        method,
                        None,
                        snapshot,
                    )
                ],
                "blockers": [],
                "metadata": {},
            }
        )
        for stage_external_id, stage_label in stages.items()
    ]

    return [season, *stage_candidates]


def candidate_recovery_residue(
    *,
    provider: str,
    entity_type: str,
    external_id: str,
    reason: str,
    candidate_ids: list[str] | None = None,
    blocker_code: str = "candidate_recovery_required",
    blocker_message: str | None = None,
    next_action: str | None = None,
    metadata: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Create a review hand-off when a candidate cannot be safely accepted."""

    return {
        "residue_id": f"review:{provider}:{entity_type}:{external_id}",
        "entity_type": entity_type,
        "provider": provider,
        "external_id": external_id,
        "reason": reason,
        "status": "open",
        "candidate_ids": list(candidate_ids or ()),
        "blockers": [
            {
                "code": blocker_code,
                "message": blocker_message or reason,
                "severity": "blocking",
                "provider": provider,
                "metadata": {},
            }
        ],
        "next_action": next_action,
        "metadata": dict(metadata or {}),
    }


def _relationship(
    provider: str,
    relationship_type: str,
    subject_external_id: str,
    object_external_id: str | None,
    subject_type: str,
    object_type: str,
    method: str,
    confidence: float | None,
    snapshot: str | None,
) -> dict[str, Any] | None:
    if not object_external_id:
        return None
    return _drop_empty(
        {
            "provider": provider,
            "relationship_type": relationship_type,
            "subject_external_id": subject_external_id,
            "object_external_id": object_external_id,
            "subject_type": subject_type,
            "object_type": object_type,
            "evidence_count": 1,
            "method": method,
            "confidence": confidence,
            "snapshot": snapshot,
        }
    )


def _drop_empty(payload: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in payload.items() if value is not None}


def _target_status(target_id: str | None, score: float | None) -> str:
    """Only mark direct-bridge certainty as accepted in portable examples."""

    if target_id and score == 1.0:
        return "accepted"
    return "review"
