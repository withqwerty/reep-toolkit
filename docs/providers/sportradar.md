---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: sportradar
entity_types: [player, team, coach, competition, season, match]
access_tier: paid_or_private
source_kind: living
authority_role: coverage_probe
bridge_providers: []
matching_fields:
  [sportradar_urn, name, date_of_birth, nationality, competitor_id, sport_event_id]
confidence_floor: 0.95
private_dependencies: []
---

# Sportradar

Sportradar is a commercial multi-sport data provider. Its football identifiers appear in
industry feeds, but there is no public bridge path equivalent to Wikidata or
Transfermarkt.

## Entity Model

| Entity type | Sportradar term       | ID shape              | Notes                                             |
| ----------- | --------------------- | --------------------- | ------------------------------------------------- |
| Player      | player                | `sr:player:{id}`      | Keep the URN prefix.                              |
| Team        | competitor            | `sr:competitor:{id}`  | Team namespace is distinct from player namespace. |
| Coach       | player/staff surfaces | URN where present     | Coverage varies.                                  |
| Competition | tournament            | `sr:tournament:{id}`  | Provider tournament namespace.                    |
| Season      | season                | `sr:season:{id}`      | Provider season namespace.                        |
| Match       | sport_event           | `sr:sport_event:{id}` | Provider match namespace.                         |

## Matching Surface

| Field                | Use                              | Gotcha                                            |
| -------------------- | -------------------------------- | ------------------------------------------------- |
| Full URN             | Provider bridge candidate.       | Do not strip the `sr:type:` prefix.               |
| DOB/name/nationality | Person evidence where available. | Subscriber metadata is not public evidence.       |
| Competitor URN       | Team bridge candidate.           | Numeric IDs collide across URN types if stripped. |
| Sport-event URN      | Match bridge candidate.          | Confirm teams, date, and competition.             |

## Reep-Style Linking Advice

- Store the whole URN, not just the numeric tail.
- Treat each URN type as a separate namespace.
- Use Sportradar as a paid-feed provider bridge only when enough metadata is available.
- Do not imply public reproducibility from subscriber-only identifiers.

## Gotchas

- Same numeric tail can mean different things under different URN types.
- No general Wikidata property or public open-data programme.
- Multi-sport scope makes type gates mandatory.

## References

- [Sportradar](https://sportradar.com/)
- [Sportradar developer portal](https://developer.sportradar.com/)
