---
doc_type: example
content_lane: example
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: examples
stance: illustrative
contribution_model: example_patch
entity_types: [team]
matching_fields: [name, country, founded, competition]
confidence_floor: 0.95
failure_mode: team_name_collision
decision: [review]
search_tags: [team, name-only, collision]
---

# Team Name Collision

Team names collide globally. This example shows why name-only matching stays below the
auto-write threshold.

## Source Record

```json
{
  "provider": "example_ratings",
  "team_id": "abc-123",
  "name": "United",
  "country": null
}
```

## Candidate Lookup

| candidate | name      | country | founded | competition     |
| --------- | --------- | ------- | ------- | --------------- |
| `t_001`   | United FC | England | 1901    | regional league |
| `t_002`   | United    | Ghana   | 1978    | premier league  |
| `t_003`   | United SC | India   | 1927    | i-league        |

No single target is safe.

## Decision

| Method      | Outcome          | Confidence | Write? |
| ----------- | ---------------- | ---------: | ------ |
| `name-only` | three candidates |     `0.80` | no     |

## Better Source Record

```json
{
  "provider": "example_ratings",
  "team_id": "abc-123",
  "name": "United SC",
  "country": "India",
  "founded": 1927
}
```

Now one candidate survives:

| Method                 | Outcome           | Confidence | Write? |
| ---------------------- | ----------------- | ---------: | ------ |
| `name+country+founded` | attach to `t_003` |     `0.95` | yes    |

## Reep-Style Lesson

Name-only team matching is candidate generation, not identity resolution. Add country,
competition, founded year, or a provider bridge before writing.
