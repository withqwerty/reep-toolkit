---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: api_football
entity_types: [player, team, coach, competition, season, match]
access_tier: paid_or_private
source_kind: living
authority_role: metadata_source
bridge_providers: []
matching_fields:
  [
    api_football_id,
    name,
    date_of_birth,
    nationality,
    country,
    team_id,
    league_id,
    fixture_id,
  ]
confidence_floor: 0.95
private_dependencies: []
---

# API-Football

API-Football is a commercial football API with broad player, team, league, season, and
fixture coverage. For identity work it is metadata-anchored: useful biographical fields,
but no first-class public bridge to Transfermarkt, Wikidata, FBref, or Opta.

## Entity Model

| Entity type | API-Football term | ID shape              | Notes                                      |
| ----------- | ----------------- | --------------------- | ------------------------------------------ |
| Player      | player            | numeric               | Separate from team and fixture namespaces. |
| Team        | team              | numeric               | Stable provider team key.                  |
| Coach       | coach             | numeric where present | Coverage varies.                           |
| Competition | league            | numeric               | Provider competition family.               |
| Season      | season            | year-like integer     | Scoped to league.                          |
| Match       | fixture           | numeric               | Provider match key.                        |

## Matching Surface

| Field                    | Use                                  | Gotcha                                             |
| ------------------------ | ------------------------------------ | -------------------------------------------------- |
| Player ID                | Provider bridge after identity gate. | Numeric IDs are type-scoped.                       |
| Full name fields         | Person candidate.                    | Display names can be abbreviated on some surfaces. |
| Birth date/place/country | Strong person evidence.              | Use detail/profile-style records when available.   |
| Nationality              | Corroboration.                       | Representation and birth country may differ.       |
| Team ID                  | Context.                             | Current team is point-in-time.                     |
| League/fixture IDs       | Structure and match candidates.      | League season still needs year/season context.     |

## Reep-Style Linking Advice

- Do not mint from API-Football name-only player rows.
- Use DOB plus normalised full name for person bridges.
- Keep player, team, league, and fixture IDs as separate provider namespaces.
- Treat fixture IDs as match bridge candidates only after teams/date/competition align.
- Preserve the source snapshot because metadata can change with transfers and squad
  updates.

## Gotchas

- No public cross-provider bridge is exposed.
- Position is coarse and only weak corroboration.
- Height and weight can be strings or missing.
- Current team is not a historical career or membership record.
- Free/evaluation coverage and paid coverage can differ materially.

## References

- [API-Football](https://www.api-football.com/)
- [API-Football documentation](https://www.api-football.com/documentation-v3)
