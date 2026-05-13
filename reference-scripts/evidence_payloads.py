#!/usr/bin/env python3
"""Reference helpers for validating portable evidence payloads.

This file is copy-paste reference code, not a package API. It validates the small
JSON shape used by the fixtures in this repository without depending on Reep internals
or a particular target register.
"""

from __future__ import annotations

import json
import unicodedata
from collections.abc import Mapping
from pathlib import Path
from typing import Any


ENTITY_TYPES = {"player", "team", "coach", "competition", "season", "stage", "match"}
SOURCE_ROLES = {"canonical_feed", "bridge", "corroborator", "context", "target_register"}
EVIDENCE_KINDS = {
    "attribute",
    "bridge",
    "fixture_tuple",
    "name",
    "relationship",
    "source_url",
    "url_handle",
}
CANDIDATE_STATUSES = {"accepted", "blocked", "deferred", "matched", "rejected", "review"}
RESIDUE_STATUSES = {"open", "resolved", "superseded", "actioned", "closed"}
BLOCKER_SEVERITIES = {"info", "warning", "blocking"}


def load_json(path: str | Path) -> Any:
    """Load a JSON fixture from disk."""

    return json.loads(Path(path).read_text())


def normalise_name(value: str) -> str:
    """Strip Latin diacritics, lowercase, and collapse surrounding whitespace."""

    decomposed = unicodedata.normalize("NFKD", value)
    stripped = "".join(char for char in decomposed if not unicodedata.combining(char))
    return " ".join(stripped.lower().split())


def validate_candidate(payload: Mapping[str, Any]) -> list[str]:
    """Return validation errors for a candidate payload."""

    errors: list[str] = []
    _require(
        payload,
        errors,
        "candidate_id",
        "entity_type",
        "provider",
        "external_id",
        "status",
    )
    _one_of(payload, errors, "entity_type", ENTITY_TYPES)
    _one_of(payload, errors, "status", CANDIDATE_STATUSES)
    _confidence(payload, errors, "score")

    for index, item in enumerate(payload.get("evidence", ())):
        errors.extend(_prefix(f"evidence[{index}]", validate_evidence(item)))

    for index, item in enumerate(payload.get("relationship_evidence", ())):
        errors.extend(
            _prefix(f"relationship_evidence[{index}]", validate_relationship(item))
        )

    for index, item in enumerate(payload.get("blockers", ())):
        errors.extend(_prefix(f"blockers[{index}]", validate_blocker(item)))

    return errors


def validate_evidence(payload: Mapping[str, Any]) -> list[str]:
    """Return validation errors for one evidence item."""

    errors: list[str] = []
    _require(payload, errors, "provider", "kind", "entity_type")
    _one_of(payload, errors, "kind", EVIDENCE_KINDS)
    _one_of(payload, errors, "entity_type", ENTITY_TYPES)
    _one_of(payload, errors, "source_role", SOURCE_ROLES, required=False)
    _confidence(payload, errors, "confidence")
    return errors


def validate_relationship(payload: Mapping[str, Any]) -> list[str]:
    """Return validation errors for one relationship-evidence item."""

    errors: list[str] = []
    _require(
        payload,
        errors,
        "provider",
        "relationship_type",
        "subject_external_id",
        "object_external_id",
        "subject_type",
        "object_type",
    )
    _one_of(payload, errors, "subject_type", ENTITY_TYPES)
    _one_of(payload, errors, "object_type", ENTITY_TYPES)
    _confidence(payload, errors, "confidence")
    if int(payload.get("evidence_count", 1)) < 1:
        errors.append("evidence_count must be at least 1")
    return errors


def validate_blocker(payload: Mapping[str, Any]) -> list[str]:
    """Return validation errors for one blocker item."""

    errors: list[str] = []
    _require(payload, errors, "code", "message", "severity")
    _one_of(payload, errors, "severity", BLOCKER_SEVERITIES)
    return errors


def validate_review_residue(payload: Mapping[str, Any]) -> list[str]:
    """Return validation errors for a review-residue payload."""

    errors: list[str] = []
    _require(
        payload,
        errors,
        "residue_id",
        "entity_type",
        "provider",
        "external_id",
        "reason",
        "status",
    )
    _one_of(payload, errors, "entity_type", ENTITY_TYPES)
    _one_of(payload, errors, "status", RESIDUE_STATUSES)

    for index, item in enumerate(payload.get("blockers", ())):
        errors.extend(_prefix(f"blockers[{index}]", validate_blocker(item)))

    return errors


def validate_source_constraints(payload: Any) -> list[str]:
    """Return validation errors for a source-constraint list."""

    errors: list[str] = []
    if not isinstance(payload, list):
        return ["source constraints payload must be a list"]

    for index, item in enumerate(payload):
        if not isinstance(item, Mapping):
            errors.append(f"[{index}] must be an object")
            continue
        _require(item, errors, "provider", "role", "entity_types")
        _one_of(item, errors, "role", SOURCE_ROLES)
        for entity_type in item.get("entity_types", ()):
            if entity_type not in ENTITY_TYPES:
                errors.append(
                    f"[{index}].entity_types contains unsupported value {entity_type!r}"
                )
        _confidence(item, errors, "min_confidence")

    return errors


def stable_json(payload: Any) -> str:
    """Serialise a payload deterministically for fixture comparison."""

    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def _require(payload: Mapping[str, Any], errors: list[str], *keys: str) -> None:
    for key in keys:
        if key not in payload or payload[key] in (None, ""):
            errors.append(f"missing required field {key!r}")


def _one_of(
    payload: Mapping[str, Any],
    errors: list[str],
    key: str,
    allowed: set[str],
    *,
    required: bool = True,
) -> None:
    if key not in payload:
        if required:
            errors.append(f"missing required field {key!r}")
        return
    if payload[key] not in allowed:
        errors.append(f"{key} has unsupported value {payload[key]!r}")


def _confidence(payload: Mapping[str, Any], errors: list[str], key: str) -> None:
    if key not in payload or payload[key] is None:
        return
    value = float(payload[key])
    if value < 0 or value > 1:
        errors.append(f"{key} must be between 0 and 1")


def _prefix(prefix: str, errors: list[str]) -> list[str]:
    return [f"{prefix}: {error}" for error in errors]
