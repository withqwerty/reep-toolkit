---
doc_type: example
content_lane: example
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: examples
stance: illustrative
contribution_model: example_patch
provider: sportmonks
entity_types: [competition, season, match]
matching_fields: [season_id, stage_id, round_id, group_id, fixture_id]
confidence_floor: 0.95
failure_mode: season_stage_flattening
decision: [write_scoped_bridges]
search_tags: [sportmonks, stage, season]
---

# SportMonks Stage And Season Mismatch

This example shows why a provider's `season_id` is not always the register season you
want. Some providers model competition structure with separate stage, round, and group
entities.

## Situation

A register models a split competition like this:

| entity_id | entity_type | name                  | parent_season_id |
| --------- | ----------- | --------------------- | ---------------- |
| `s_2024`  | season      | Liga Example 2024     | null             |
| `s_2024a` | season      | Liga Example Apertura | `s_2024`         |
| `s_2024c` | season      | Liga Example Clausura | `s_2024`         |

The provider fixture says:

```json
{
  "provider": "sportmonks",
  "fixture_id": 90001,
  "league_id": 501,
  "season_id": 8000,
  "stage_id": 8101,
  "round_id": 8205,
  "group_id": null,
  "name": "Riverside FC v Central FC",
  "date": "2024-08-10"
}
```

The provider's `season_id` identifies the broad competition season. The `stage_id`
identifies Apertura or Clausura.

## Bad Bridge

```text
sportmonks:season:8000 -> s_2024a
```

This flattens the provider's broad season onto one leaf stage. Future Clausura fixtures
with the same `season_id` will now appear to belong to Apertura.

## Correct Model

Represent the provider fields at their actual level:

| Provider field | Register target                 | Reason                              |
| -------------- | ------------------------------- | ----------------------------------- |
| `league_id`    | competition family              | Provider league is the competition. |
| `season_id`    | parent season                   | It spans multiple stages.           |
| `stage_id`     | leaf season or stage entity     | It distinguishes Apertura/Clausura. |
| `round_id`     | round metadata or fixture field | Usually not a register entity.      |
| `fixture_id`   | match bridge                    | First-class fixture identity.       |

## Write Set

```text
entity_id: s_2024
provider: sportmonks
external_id: season:8000
confidence: 0.95
method: provider-season-parent
```

```text
entity_id: s_2024a
provider: sportmonks
external_id: stage:8101
confidence: 0.95
method: provider-stage-leaf
```

```text
entity_id: m_90001
provider: sportmonks
external_id: fixture:90001
confidence: 1.0
method: direct-fixture-bridge
```

## Validation Checks

Check that:

- every fixture bridge carries the provider fixture ID,
- every stage bridge points to a leaf season or stage,
- every provider `season_id` used across multiple stages maps to a parent season,
- no leaf season claims the same provider `season_id` unless the provider docs prove the
  season has no sub-stage split.

## Doctrine Demonstrated

- Understand the provider world model before writing bridges.
- IDs identify provider objects, not necessarily register objects.
- Stage-aware matching prevents seasonal drift in split competitions.
- A correct bridge may need typed external IDs such as `season:8000` and `stage:8101`.
