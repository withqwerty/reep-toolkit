---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: livesport
entity_types: [player, team, coach, competition, match]
access_tier: public_grey
source_kind: living
authority_role: bridge_source
bridge_providers: [wikidata]
matching_fields:
  [soccerway_id, flashscore_id, besoccer_id, name, date_of_birth, nationality, team_id]
confidence_floor: 1.0
private_dependencies: []
---

# Livesport Ecosystem

This card covers the identity-relevant public surfaces around Soccerway, Flashscore, and
BeSoccer. They share ecosystem context, but their ID systems remain independent and must
be stored as separate provider namespaces.

## Entity Model

| Surface    | Entity types                     | ID shape                                | Notes                                                  |
| ---------- | -------------------------------- | --------------------------------------- | ------------------------------------------------------ |
| Soccerway  | person, team, competition, match | legacy numeric plus newer slug-like IDs | Legacy numeric IDs are widely represented in Wikidata. |
| Flashscore | player, team, match, competition | slug plus alphanumeric key              | Sparse but useful Wikidata bridge properties.          |
| BeSoccer   | player and team surfaces         | slug/provider key                       | Useful where Wikidata properties exist.                |

## Matching Surface

| Field                   | Use                                    | Gotcha                                              |
| ----------------------- | -------------------------------------- | --------------------------------------------------- |
| Soccerway legacy ID     | Strong public bridge through Wikidata. | Person property can cover players and coaches.      |
| Soccerway newer ID/slug | Migration candidate.                   | Keep separate from legacy numeric ID until mapped.  |
| Flashscore ID           | Public bridge where Wikidata has it.   | Coverage is sparse.                                 |
| Date of birth           | Strong person signal where present.    | Date display formats differ by surface.             |
| Team ID/name            | Context.                               | Ecosystem ownership does not imply shared team IDs. |

## Bridge Surface

| Bridge route                      | Use                          | Caution                                                  |
| --------------------------------- | ---------------------------- | -------------------------------------------------------- |
| Wikidata → Soccerway person/team  | Strong legacy public bridge. | Keep player/coach semantics explicit.                    |
| Wikidata → Flashscore player/team | Strong where present.        | Sparse compared with Soccerway.                          |
| Wikidata → BeSoccer person        | Useful extra public bridge.  | Coverage is partial.                                     |
| Soccerway legacy → newer URL form | Migration evidence.          | Record both forms rather than overwriting one namespace. |

## Reep-Style Linking Advice

- Keep Soccerway, Flashscore, and BeSoccer as separate provider namespaces.
- Use Wikidata properties as the preferred public bridge route.
- Treat scheme migrations as relationship/provenance evidence, not a reason to delete
  legacy IDs.
- Do not infer a Flashscore ID from a Soccerway ID or vice versa.

## Gotchas

- Soccerway person IDs can apply to players and coaches.
- Newer Soccerway URL forms should not be collapsed into legacy IDs without a recorded
  mapping.
- Flashscore slugs can use name ordering conventions that differ from display names.
- Shared ecosystem context does not mean shared registry identity.

## References

- [Soccerway](https://www.soccerway.com/)
- [Flashscore](https://www.flashscore.com/)
- [BeSoccer](https://www.besoccer.com/)
- [Livesport](https://www.livesport.eu/)
- Wikidata [P2369](https://www.wikidata.org/wiki/Property:P2369),
  [P6131](https://www.wikidata.org/wiki/Property:P6131),
  [P8259](https://www.wikidata.org/wiki/Property:P8259),
  [P7876](https://www.wikidata.org/wiki/Property:P7876),
  [P12577](https://www.wikidata.org/wiki/Property:P12577)
