---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: sofifa
entity_types: [player, team, competition]
access_tier: public_grey
source_kind: living
authority_role: metadata_source
bridge_providers: [wikidata]
matching_fields:
  [sofifa_id, edition, name, date_of_birth, nationality, team_id, foot, position]
confidence_floor: 0.95
private_dependencies: []
---

# SoFIFA

SoFIFA mirrors EA Sports FC / FIFA player and team data. It is useful because the player
attribute surface is rich, but player IDs can drift by game edition and should be
treated as edition-scoped unless verified.

## Entity Model

| Entity type | SoFIFA term     | ID shape                     | Notes                                        |
| ----------- | --------------- | ---------------------------- | -------------------------------------------- |
| Player      | player          | numeric plus edition/version | Can change across editions for some players. |
| Team        | team            | numeric                      | More stable than player IDs.                 |
| Competition | league          | numeric                      | Game competition context.                    |
| Season      | edition/version | game edition                 | Not a football season entity.                |
| Match       | none            | —                            | Not modelled.                                |

## Matching Surface

| Field                  | Use                        | Gotcha                                        |
| ---------------------- | -------------------------- | --------------------------------------------- |
| Player ID + edition    | Provider bridge candidate. | Re-verify across editions.                    |
| Full name/display name | Person candidate.          | Display names often use initials.             |
| Date of birth          | Strong person signal.      | Still needs edition/version provenance.       |
| Nationality            | Corroboration.             | Country labels can vary by edition.           |
| Foot/height/position   | Useful tie-breakers.       | Game attributes are not identity proof alone. |
| Team ID                | Team bridge candidate.     | Team names can change with licensing.         |

## Reep-Style Linking Advice

- Store player IDs with edition/version context.
- Treat Wikidata SoFIFA claims as edition-specific leads.
- Use DOB, full name, nationality, foot, and team context for player bridges.
- Prefer team IDs for team bridge experiments; player IDs need stronger maintenance.

## Gotchas

- Player IDs can drift silently between editions.
- Display names often use initial plus surname.
- Team names can change for licensing reasons while team IDs remain more stable.
- Women's coverage is newer and should be audited separately.

## References

- [SoFIFA](https://sofifa.com/)
- [EA Sports FC](https://www.ea.com/games/ea-sports-fc)
- [Wikidata P1469](https://www.wikidata.org/wiki/Property:P1469)
