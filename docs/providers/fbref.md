---
doc_type: provider_card
content_lane: reference
status: review_ready
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: fbref
entity_types: [player, team, coach, competition, match]
access_tier: public_grey
source_kind: living
authority_role: bridge_spine
bridge_providers: [wikidata, transfermarkt]
matching_fields:
  [fbref_id, name, date_of_birth, nationality, country, squad_id, competition_id]
confidence_floor: 0.95
private_dependencies: []
---

# FBref

FBref is Sports Reference's football statistics site. Its IDs are stable and widely used
in public football analytics, especially through Wikidata and community mapping
datasets.

## Why It Matters Before You Start

FBref is often the most convenient public stats-side ID. It is also easy to misuse
because the same eight-character ID format appears under players, managers, squads, and
matches. Entity type and URL path are part of the identity.

## Entity Model

| Entity type | URL family        | ID shape                 | Notes                              |
| ----------- | ----------------- | ------------------------ | ---------------------------------- |
| Player      | `/players/{id}/`  | 8-character alphanumeric | Stable player page.                |
| Coach       | `/managers/{id}/` | 8-character alphanumeric | Separate from player ID.           |
| Team        | `/squads/{id}/`   | 8-character alphanumeric | FBref calls teams squads.          |
| Competition | `/comps/{id}/`    | numeric                  | Competition family.                |
| Season      | URL path segment  | year pair                | Not normally a separate entity ID. |
| Match       | `/matches/{id}/`  | 8-character alphanumeric | Separate match namespace.          |

## Matching Surface

| Field         | Use                                      | Gotcha                                                  |
| ------------- | ---------------------------------------- | ------------------------------------------------------- |
| FBref ID      | Strong bridge when entity type is known. | Same shape across different entity types.               |
| Name          | Display and signal matching.             | Usually clean, accents preserved.                       |
| Date of birth | Strong player/coach signal.              | Available through wrappers for many players.            |
| Nationality   | Corroboration.                           | Uses football/FIFA-style country codes, not always ISO. |
| Squad ID      | Team context.                            | "Squad" is FBref's team term.                           |
| Birth name    | Secondary person signal.                 | Present only for some people.                           |
| Position      | Weak corroboration.                      | Multi-position strings are comma-joined and coarse.     |

## Bridge Surface

| Bridge route                           | Use                               | Caution                                                              |
| -------------------------------------- | --------------------------------- | -------------------------------------------------------------------- |
| Wikidata → FBref player/coach          | Primary public ID bridge.         | Property is shared across player and coach pages; carry entity type. |
| Wikidata → FBref team                  | Strong team bridge where present. | Team is called squad on FBref.                                       |
| Wikidata → FBref competition           | Useful competition bridge.        | Lower-tier and historical coverage is patchier.                      |
| Transfermarkt ↔ FBref mapping datasets | Strong public bridge evidence.    | Treat dataset version and source as provenance.                      |

## Reep-Style Linking Advice

- Treat Wikidata FBref properties as the primary public bridge.
- Use community Transfermarkt-FBref mappings as strong but auditable evidence.
- Carry entity type everywhere; `abc12345` alone is not enough.
- Respect Sports Reference bot policy; prefer Wikidata or public mapping datasets when
  all you need is IDs.

## Gotchas

- Coach and player IDs are separate for the same human.
- Nationality code systems need mapping before comparison.
- The same eight-character visual shape is used by player, manager, squad, and match
  pages; URL family is part of the identifier.
- Player nationalities use football/FIFA-style codes such as `ENG`, `SCO`, `WAL`, and
  `NIR`, which do not map one-to-one to ISO country codes.
- Lower-tier and historical coverage is uneven.
- Scraping is rate-limited and should not be your default identity extraction path.

## References

- [FBref](https://fbref.com/en/)
- [Sports Reference bot policy](https://www.sports-reference.com/bot-traffic.html)
- Wikidata [P5750](https://www.wikidata.org/wiki/Property:P5750),
  [P8642](https://www.wikidata.org/wiki/Property:P8642),
  [P13664](https://www.wikidata.org/wiki/Property:P13664)
- [worldfootballR_data](https://github.com/JaseZiv/worldfootballR_data)
