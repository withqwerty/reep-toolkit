---
doc_type: schema_reference
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: templates
stance: descriptive
contribution_model: example_patch
entity_types: [player, team, coach, competition, season, match]
---

# Evidence Payload Schema

The toolkit fixtures use a small JSON shape for candidate links, evidence, blockers,
relationship evidence, and review residue. It is not a mandated API contract; it is a
portable shape that examples and reference scripts can share.

## Candidate

| Field                   | Meaning                                                                        |
| ----------------------- | ------------------------------------------------------------------------------ |
| `candidate_id`          | Stable ID for this candidate payload.                                          |
| `entity_type`           | Target entity type: player, team, coach, competition, season, stage, or match. |
| `provider`              | Source provider proposing the candidate.                                       |
| `external_id`           | Provider-native ID for the source row.                                         |
| `target_label`          | Human-readable target label when known.                                        |
| `score`                 | Confidence label or matcher score.                                             |
| `method`                | Matcher/template method label.                                                 |
| `status`                | Suggested route such as `matched`, `review`, `deferred`, or `rejected`.        |
| `evidence`              | Attribute or bridge evidence records.                                          |
| `relationship_evidence` | Relationship context such as team, match, season, or lineup links.             |
| `blockers`              | Reasons the candidate cannot be written automatically.                         |
| `metadata`              | Extra public-safe diagnostic context.                                          |

## Evidence

Evidence records explain why a candidate exists.

| Field         | Meaning                                                                        |
| ------------- | ------------------------------------------------------------------------------ |
| `provider`    | Provider supplying the evidence.                                               |
| `kind`        | Evidence kind: `bridge`, `attribute`, `fixture_tuple`, `name`, or similar.     |
| `entity_type` | Entity type the evidence describes.                                            |
| `external_id` | Provider-native ID for the source row.                                         |
| `value`       | Optional structured value, such as DOB/name or fixture tuple.                  |
| `source_role` | Role such as `canonical_feed`, `bridge`, `corroborator`, or `metadata_source`. |
| `method`      | Method that produced the evidence.                                             |
| `confidence`  | Confidence label for this evidence item.                                       |
| `snapshot`    | Source snapshot or export label.                                               |

## Relationship Evidence

Relationship evidence narrows candidates. It does not replace identity evidence.

| Field                          | Meaning                                                                             |
| ------------------------------ | ----------------------------------------------------------------------------------- |
| `relationship_type`            | Relationship being asserted, such as `home_team`, `season`, or `appeared_for_team`. |
| `subject_external_id`          | Provider-native subject ID.                                                         |
| `object_external_id`           | Provider-native object ID.                                                          |
| `subject_type` / `object_type` | Entity types on either side.                                                        |
| `evidence_count`               | Number of rows supporting the relationship.                                         |
| `method`                       | Method that summarised the relationship.                                            |
| `confidence`                   | Confidence label for the relationship evidence.                                     |

## Blocker

Blockers are explicit reasons a candidate should not be written yet.

| Field      | Meaning                               |
| ---------- | ------------------------------------- |
| `code`     | Stable blocker code.                  |
| `message`  | Human-readable explanation.           |
| `severity` | `blocking`, `warning`, or `info`.     |
| `provider` | Provider associated with the blocker. |
| `metadata` | Optional public-safe detail.          |

Common blocker codes include:

- `competition_not_mapped`
- `candidate_recovery_required`
- `ambiguous_candidate`
- `missing_identity_guard`
- `provider_namespace_unclear`

## Review Residue

Review residue is the payload left behind when a candidate is plausible but cannot be
accepted automatically.

| Field           | Meaning                                                |
| --------------- | ------------------------------------------------------ |
| `residue_id`    | Stable review-residue ID.                              |
| `entity_type`   | Entity type under review.                              |
| `provider`      | Source provider.                                       |
| `external_id`   | Provider-native row ID.                                |
| `reason`        | Short reason for review or deferral.                   |
| `status`        | Review status such as `open`, `actioned`, or `closed`. |
| `candidate_ids` | Candidate payloads related to the review item.         |
| `blockers`      | Blocking issues that need resolution.                  |
| `next_action`   | Suggested public-safe next step.                       |

## Fixtures

The current synthetic fixtures are listed in [Portable Templates](README.md). Every
fixture should load as JSON, use invented provider IDs, and avoid private paths or
production identifiers.
