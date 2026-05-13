---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: sportec
entity_types: [player, team, competition, season, match]
access_tier: mixed
source_kind: living
authority_role: corroborator
bridge_providers: []
matching_fields:
  [sportec_id, dfl_id, name, date_of_birth, country, team_id, match_id, season]
confidence_floor: 0.95
private_dependencies: []
---

# Sportec Solutions

Sportec Solutions is the Bundesliga's official data arm. Its public identity value is
mostly educational: a small open-data footprint shows the Sportec/DFL XML shape, while
full coverage sits in commercial league feeds.

## Entity Model

| Entity type | Sportec / DFL term     | ID shape               | Notes                                             |
| ----------- | ---------------------- | ---------------------- | ------------------------------------------------- |
| Player      | Person                 | DFL-prefixed object ID | Strong when DOB/name/country metadata is present. |
| Team        | Club                   | DFL-prefixed club ID   | Bundesliga-specific context.                      |
| Match       | Match                  | DFL-prefixed match ID  | Match identity inside the Sportec feed.           |
| Competition | Competition/feed scope | provider-scoped        | Usually Bundesliga or Bundesliga 2 context.       |
| Season      | Season                 | season string          | Feed-scoped season context.                       |

## Matching Surface

| Field                | Use                                | Gotcha                                                   |
| -------------------- | ---------------------------------- | -------------------------------------------------------- |
| Person ID            | Provider bridge after person gate. | DFL IDs are not public cross-provider IDs.               |
| Birth date           | Strong person evidence.            | Normalise date formats before comparison.                |
| Country and position | Corroboration.                     | Some labels can be German-language or provider-specific. |
| Team ID              | Team bridge candidate.             | Coverage is Bundesliga-shaped.                           |
| Match ID             | Match bridge candidate.            | Confirm teams, date, and competition context.            |

## Reep-Style Linking Advice

- Treat Sportec IDs as provider-scoped commercial identifiers.
- Use the open sample for format and parser understanding, not coverage claims.
- Use DOB, name, country, team, and match context together for person resolution.
- Map granular German position labels to a coarser vocabulary before using them as
  corroboration.

## Gotchas

- Public open data is small compared with the commercial feed.
- There is no general Wikidata bridge for Sportec IDs.
- Event and tracking data can share one feed shape, but tracking fields are not identity
  attributes.

## References

- [Sportec Solutions](https://www.sportec-solutions.de/)
- [DFL](https://www.dfl.de/)
- [Sportec open-data paper](https://doi.org/10.1038/s41597-025-04505-y)
- [kloppy](https://github.com/PySport/kloppy)
