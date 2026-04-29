---
doc_type: example
content_lane: example
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: examples
stance: illustrative
contribution_model: example_patch
entity_types: [competition, season]
matching_fields: [provider_id, competition_id, season_label, namespace]
confidence_floor: 1.0
failure_mode: structural_provider_id_collision
decision: [rewrite_namespace]
search_tags: [season, namespace, validator]
---

# Structural Season ID Collision

This example shows why a duplicate provider-ID report is not always a duplicate entity
bug. Sometimes the provider ID was stored without enough context.

## Situation

A provider uses a bare year as the season value inside each competition:

| competition_provider_id | competition_name | provider_season_value | display_label |
| ----------------------- | ---------------- | --------------------- | ------------- |
| `comp_1`                | Premier Division | `2024`                | 2024          |
| `comp_2`                | National Cup     | `2024`                | 2024          |
| `comp_3`                | Second Division  | `2024`                | 2024          |

The register has three distinct season entities:

| entity_id | name                  |
| --------- | --------------------- |
| `s_001`   | 2024 Premier Division |
| `s_002`   | 2024 National Cup     |
| `s_003`   | 2024 Second Division  |

## Bad Bridge Shape

```text
s_001 -> provider:2024
s_002 -> provider:2024
s_003 -> provider:2024
```

A validator flags duplicate same-provider season IDs. The report is real, but the cause
is structural: `2024` is not a globally unique season ID.

## Correct Bridge Shape

Store the provider ID at the level it actually identifies:

```text
s_001 -> provider:comp_1:season:2024
s_002 -> provider:comp_2:season:2024
s_003 -> provider:comp_3:season:2024
```

Or store separate fields:

| entity_id | provider | competition_external_id | season_external_id |
| --------- | -------- | ----------------------- | ------------------ |
| `s_001`   | provider | `comp_1`                | `2024`             |
| `s_002`   | provider | `comp_2`                | `2024`             |
| `s_003`   | provider | `comp_3`                | `2024`             |

## Validator Interpretation

| Duplicate shape                                              | Meaning                   | Action                 |
| ------------------------------------------------------------ | ------------------------- | ---------------------- |
| Same provider, same bare year, different competitions        | structural namespace bug  | rewrite bridge shape   |
| Same provider, same scoped season ID, same competition       | possible duplicate season | review/merge           |
| Same provider, same scoped season ID, different entity types | type-scope issue          | inspect provider model |

## Migration Plan

1. Identify all bare season-year bridges.
2. Join each bridge to the provider competition ID.
3. Rewrite accepted bridge keys into scoped IDs.
4. Preserve old bare-year values as source fields, not global bridge IDs.
5. Re-run duplicate-provider checks.

## Doctrine Demonstrated

- Provider IDs identify provider objects, not necessarily global register objects.
- Validators need provider-world-model context.
- Structural collisions should be fixed by namespacing, not by merging unrelated
  seasons.
- A bare display year is usually metadata, not a stable bridge.
