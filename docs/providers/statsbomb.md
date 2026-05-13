---
doc_type: provider_card
content_lane: reference
status: review_ready
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: statsbomb
entity_types: [player, team, coach, competition, season, match]
access_tier: public_bulk
source_kind: mixed
authority_role: corroborator
bridge_providers: []
matching_fields:
  [
    statsbomb_id,
    name,
    date_of_birth,
    country,
    team_id,
    competition_id,
    season_id,
    match_id,
  ]
confidence_floor: 0.95
private_dependencies: []
---

# StatsBomb

StatsBomb is a football event-data provider with a well-known public Open Data subset
and broader licensed data products. For identity work, its strongest public value is
covered-match structure, lineups, teams, players, and stable provider-scoped IDs within
the StatsBomb dataset.

## Why It Matters Before You Start

StatsBomb Open Data is one of the best public examples for testing football data
pipelines, but its coverage is selective. A missing entity in Open Data is not evidence
that the entity is absent from StatsBomb as a provider.

The safe posture is to treat StatsBomb IDs as strong within a StatsBomb snapshot, and as
candidate/corroborating evidence in a wider register unless another source supplies the
missing person attributes.

## Entity Model

| Entity type | StatsBomb term | ID shape              | Notes                                                                 |
| ----------- | -------------- | --------------------- | --------------------------------------------------------------------- |
| Player      | player         | numeric               | Appears in lineups and events.                                        |
| Team        | team           | numeric               | Appears in matches, lineups, and events.                              |
| Coach       | manager        | numeric where present | Usually match/team metadata rather than a complete staff register.    |
| Competition | competition    | numeric               | Paired with season.                                                   |
| Season      | season         | numeric               | Provider-scoped; do not treat as globally unique without competition. |
| Match       | match          | numeric               | Strong match bridge for covered matches.                              |
| Event       | event          | UUID/string           | Event-grain data, not a register entity by default.                   |

## Matching Surface

| Field                          | Use                                 | Gotcha                                                                     |
| ------------------------------ | ----------------------------------- | -------------------------------------------------------------------------- |
| `player_id`                    | Provider-scoped player bridge.      | Needs name/team/DOB corroboration before becoming a person bridge.         |
| `player_name` / nickname       | Alias and display evidence.         | Names can be display-oriented; use another authority for DOB where needed. |
| `birth_date`                   | Strong person signal where present. | Sparse in public surfaces.                                                 |
| `team_id`                      | Provider-scoped team bridge.        | Check whether provider-side historical segmentation matches your ontology. |
| `competition_id` + `season_id` | Structural context.                 | Season ID should stay competition-scoped.                                  |
| `match_id`                     | Strong match bridge.                | Confirm teams/date/competition when linking to another register.           |
| Lineup membership              | Relationship evidence.              | Match-grain lineup evidence is not a contract or season membership edge.   |

## Bridge Surface

| Bridge route                             | Use                                                   | Caution                                                        |
| ---------------------------------------- | ----------------------------------------------------- | -------------------------------------------------------------- |
| StatsBomb match → register match         | `match_id` plus date/team/competition resolution.     | Coverage is selective in Open Data.                            |
| StatsBomb team → register team           | Team ID plus name/country/competition context.        | Provider segmentation can differ from a register's team model. |
| StatsBomb player → register person       | Name + DOB where available, plus team/lineup context. | DOB is not guaranteed; name-only should route to review.       |
| StatsBomb lineup → relationship evidence | Matchday squad/appearance context.                    | Do not convert directly into season-long membership.           |

## Reep-Style Linking Advice

- Keep StatsBomb IDs provider-scoped and snapshot-scoped.
- Use Open Data for public examples and corroboration, not as proof of full provider
  coverage.
- For people, require DOB or another source authority before accepting a bridge.
- Treat lineups as match-grain relationship evidence.
- Use match and team structure to narrow candidates, not to replace person identity
  evidence.

## Gotchas

- Open Data coverage is curated and selective.
- Country IDs are provider-internal; compare country names or normalised country
  mappings instead of raw IDs.
- Position can be match/event-specific and can change during a match.
- Event UUIDs are useful for event processing, but they are not entity-register IDs.
- Public Open Data may include rich international matches without full tournament squad
  or call-up semantics.

## References

- [StatsBomb](https://statsbomb.com/)
- [StatsBomb Open Data](https://github.com/statsbomb/open-data)
- [Hudl StatsBomb announcement](https://www.hudl.com/blog/hudl-statsbomb-press-release-en)
- [kloppy](https://github.com/PySport/kloppy)
- [mplsoccer](https://github.com/andrewRowlinson/mplsoccer)
- [socceraction](https://github.com/ML-KULeuven/socceraction)
