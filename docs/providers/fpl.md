---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: fpl
entity_types: [player, team, competition, season]
access_tier: public_api
source_kind: living
authority_role: bridge_source
bridge_providers: [opta, transfermarkt]
matching_fields: [fpl_id, opta_numeric, premier_league_id, name, team_code, season]
confidence_floor: 1.0
private_dependencies: []
---

# Fantasy Premier League

Fantasy Premier League is a public Premier League data surface. Its main identity value
is not fantasy scoring: it exposes useful Premier League and Opta-related identifiers
for current and recent Premier League players.

## Entity Model

| Entity type           | FPL term         | ID shape              | Notes                                           |
| --------------------- | ---------------- | --------------------- | ----------------------------------------------- |
| Player                | element          | season-scoped numeric | FPL's own per-season player row.                |
| Team                  | team             | season-scoped numeric | FPL team row for that season.                   |
| Opta numeric player   | code             | numeric               | Public bridge to `opta_numeric`.                |
| Opta numeric team     | team_code        | numeric               | Public team bridge; not the same as FPL `team`. |
| Premier League player | id/code surfaces | numeric where present | Distinct from `opta_numeric`.                   |

## Matching Surface

| Field             | Use                           | Gotcha                                                  |
| ----------------- | ----------------------------- | ------------------------------------------------------- |
| `code`            | `opta_numeric` player bridge. | Not a modern Opta UUID.                                 |
| `team_code`       | `opta_numeric` team bridge.   | Not the FPL per-season team ID.                         |
| `id` / element ID | FPL row identity.             | Season-scoped and not stable enough as a person bridge. |
| Name fields       | Alias evidence.               | Web names can be shortened.                             |
| Team ID           | Current-season context.       | Transfers and loans require snapshot date.              |

## Reep-Style Linking Advice

- Store FPL `code` as `opta_numeric`, not `fpl_code`.
- Keep FPL row IDs season-scoped.
- Use FPL for Premier League public bridging and sanity checks, not full football
  coverage.
- Combine FPL with Transfermarkt bridge datasets when available.

## Gotchas

- `code` and `team_code` are Opta numeric surfaces, not modern Opta UUIDs.
- FPL `team` is a fantasy-season table key, not a durable provider team bridge.
- Player web names are display names and can be shortened.
- Coverage is Premier League-only.

## References

- [FPL bootstrap API](https://fantasy.premierleague.com/api/bootstrap-static/)
- [vaastav/Fantasy-Premier-League](https://github.com/vaastav/Fantasy-Premier-League)
- [ChrisMusson/FPL-ID-Map](https://github.com/ChrisMusson/FPL-ID-Map)
- [Opta / Stats Perform](opta.md)
