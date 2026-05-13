---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: football_data_co_uk
entity_types: [team, competition, season, match]
access_tier: public_bulk
source_kind: static
authority_role: corroborator
bridge_providers: []
matching_fields: [division_code, season_code, date, home_team, away_team, score]
confidence_floor: 0.90
private_dependencies: []
---

# Football-Data.co.uk

Football-Data.co.uk is a long-running public results and odds archive. It is useful for
match-result corroboration and historical fixture work, but it is not a player or coach
identity source.

## Entity Model

| Entity type | Provider term    | ID shape        | Notes                                                      |
| ----------- | ---------------- | --------------- | ---------------------------------------------------------- |
| Match       | CSV row          | tuple           | Division, date, home, away, and score form the usable key. |
| Team        | team string      | name            | Display names vary by era and division.                    |
| Competition | division         | short code      | Provider-specific division code.                           |
| Season      | season path/code | short year pair | Provider-specific season context.                          |

## Matching Surface

| Field                  | Use                    | Gotcha                                                |
| ---------------------- | ---------------------- | ----------------------------------------------------- |
| Division code          | Competition candidate. | Codes are provider conventions.                       |
| Date                   | Match candidate.       | Day-first parsing and older season formats need care. |
| Home/Away team strings | Match/team context.    | Abbreviations and historical names vary.              |
| Full-time score        | Corroboration.         | Score alone is never identity.                        |
| Bookmaker/stat columns | Not identity.          | Useful downstream only after match is resolved.       |

## Reep-Style Linking Advice

- Use as a match-results corroborator, not a canonical entity source.
- Match on division, season, date, home team, away team, and score together.
- Keep a provider-specific team-name alias table for historical abbreviations.
- Do not infer player or coach identities; they are out of scope.

## Gotchas

- Dates are day-first and older files can use shorter year formats.
- Team names can be abbreviated or renamed across time.
- Division codes are not general competition IDs.
- There is no provider match ID beyond the row context.

## References

- [Football-Data.co.uk](https://www.football-data.co.uk/)
