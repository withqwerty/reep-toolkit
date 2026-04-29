---
doc_type: pipeline
content_lane: practice
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: pipelines
stance: opinionated
contribution_model: maintainer_doctrine
---

# Writes and Lineage

Every write should explain itself.

## Recommended Mapping Fields

| Field                       | Purpose                                                       |
| --------------------------- | ------------------------------------------------------------- |
| `entity_id`                 | Target register entity.                                       |
| `provider`                  | Canonical provider namespace.                                 |
| `external_id`               | Provider-native ID.                                           |
| `source`                    | Human-readable source label.                                  |
| `confidence`                | Routing confidence label.                                     |
| `method`                    | Matcher method, such as `bridge:transfermarkt` or `dob+name`. |
| `source_snapshot`           | Exact upstream data version.                                  |
| `matcher_version`           | Version of matching logic.                                    |
| `review_status`             | Optional human-review state.                                  |
| `created_at` / `updated_at` | Audit timestamps.                                             |

## Confidence-Aware Upserts

Default rule:

> Do not overwrite stronger evidence with weaker evidence.

If a provider mapping already exists, a rerun can update lineage and timestamps only
when the new evidence is at least as strong under the register's policy. Stronger
evidence can replace weaker evidence, but the old evidence should remain available in
history if possible.

## Review States

Suggested states:

- `auto_accepted`,
- `needs_review`,
- `accepted`,
- `rejected`,
- `superseded`.

Rejected candidates should be retained so reruns avoid repeated noise.
