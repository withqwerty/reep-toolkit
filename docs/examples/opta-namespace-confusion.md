---
doc_type: example
content_lane: example
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: examples
stance: illustrative
contribution_model: example_patch
provider: opta
entity_types: [player, team, competition, season]
matching_fields: [opta_uuid, opta_numeric, optacore]
confidence_floor: 1.0
failure_mode: provider_namespace_mismatch
decision: [reject, review]
search_tags: [opta, namespace, format-check]
---

# Opta Namespace Confusion

This example shows why `opta`, `opta_numeric`, and `optacore` must be separate provider
namespaces.

## Bad Input

A source record says:

```json
{
  "provider": "opta",
  "external_id": "244851",
  "entity_type": "player",
  "name": "Example Player"
}
```

The value is numeric, but modern Opta player IDs are 25-character alphanumeric strings.
This is probably `opta_numeric`, not `opta`.

## Namespace Checks

| Namespace      | Expected shape                   | Input `244851` valid? |
| -------------- | -------------------------------- | --------------------- |
| `opta`         | 25-character alphanumeric        | no                    |
| `opta_numeric` | numeric                          | yes                   |
| `optacore`     | numeric, competition/season only | no for player         |

## Decision

| Proposed write                                | Outcome  | Reason                                           |
| --------------------------------------------- | -------- | ------------------------------------------------ |
| `provider=opta`, `external_id=244851`         | reject   | Wrong namespace shape.                           |
| `provider=opta_numeric`, `external_id=244851` | possible | Only if source proves it is legacy Opta numeric. |

## Review Item

```text
status: needs_review
reason: opta namespace mismatch
source_value: 244851
proposed_provider: opta
suggested_provider: opta_numeric
```

## Reep-Style Lesson

Do not let generic "Opta ID" labels into the register. Namespace validation catches bad
writes before they become production bridges.
