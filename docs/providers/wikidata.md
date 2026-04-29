---
doc_type: provider_card
content_lane: reference
status: review_ready
public_safe: true
last_verified: 2026-04-29
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: wikidata
entity_types: [player, team, coach, competition, season, match]
access_tier: public_bulk
source_kind: living
authority_role: bridge_spine
bridge_providers:
  [
    transfermarkt,
    fbref,
    soccerway,
    sofascore,
    flashscore,
    premier_league,
    espn,
    soccerbase,
    uefa,
    soccerdonna,
  ]
matching_fields:
  [qid, label, alias, date_of_birth, nationality, external_id, country, competition]
confidence_floor: 1.0
private_dependencies: []
---

# Wikidata

Wikidata is the strongest public bridge spine in football identity work. It is not a
football provider in the normal product sense; it is a public knowledge graph where QIDs
connect football entities to dozens of provider-specific external IDs.

## Why It Matters Before You Start

If a player, team, coach, competition, or season has a good Wikidata item, you often get
a bundle of cross-provider IDs for free. That makes Wikidata the first place to check
before writing custom matching code.

The trap is that Wikidata is community-maintained. It is broad, public, and stable, but
it is not always complete, current, or precise enough to be your only source of truth.

## Entity Model

| Entity type | Wikidata identity                                        | Register consequence                                                                 |
| ----------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Player      | Human QID with footballer occupation or football claims. | Strong bridge hub when DOB and external IDs are present.                             |
| Coach       | Human QID with manager occupation or coach IDs.          | Often overlaps with player identity; keep provider coach/player namespaces distinct. |
| Team        | Club/team QID with football sport claims.                | Useful for names, aliases, country, and provider IDs.                                |
| Competition | League/cup QID.                                          | Good public competition spine, but stage/season modelling varies.                    |
| Season      | Season QID pointing to parent competition.               | Useful but unevenly populated outside major competitions.                            |
| Match       | Some matches have QIDs.                                  | Coverage is too sparse to rely on as a general match spine.                          |

## Matching Surface

| Field         | Use                             | Gotcha                                                               |
| ------------- | ------------------------------- | -------------------------------------------------------------------- |
| QID           | Stable public identifier.       | Merges redirect; preserve your own published IDs across QID changes. |
| English label | Display and rough match signal. | Missing labels can fall back to `Q123` strings in some query paths.  |
| Aliases       | Search and name matching.       | Aliases are not identity proof by themselves.                        |
| Date of birth | Strong player/coach signal.     | Check precision; year-only DOB is not enough for strict matching.    |
| Nationality   | Corroboration.                  | Multiple values are normal.                                          |
| External IDs  | Bridge surface.                 | Property coverage varies by country, gender, level, and era.         |

## Bridge Fields to Know

Important football properties include:

| Provider      | Player/person               | Team   | Competition | Notes                                   |
| ------------- | --------------------------- | ------ | ----------- | --------------------------------------- |
| Transfermarkt | P2446 player, P2447 manager | P7223  | P12758      | Most important public bridge target.    |
| FBref         | P5750 player/coach          | P8642  | P13664      | Strong for Sports Reference ecosystem.  |
| Soccerway     | P2369 person                | P6131  | —           | Legacy URL scheme history matters.      |
| Sofascore     | P12302 player               | P13897 | —           | Useful live-score bridge where present. |
| Flashscore    | P8259 player                | P7876  | —           | Mixed legacy/newer ID shapes.           |
| Soccerdonna   | P4381 player, P8134 coach   | P7878  | —           | High-value women's-football bridge.     |
| Opta numeric  | P8736 player                | P8737  | P8735       | Numeric legacy Opta, not modern UUID.   |

## Reep-Style Linking Advice

- Treat QID and external-ID bridges as strong evidence when entity type is clear.
- Do not let a Wikidata refresh delete or rewrite your own published entity IDs.
- Store Wikidata-derived bridges as derived evidence so they can be rebuilt.
- Keep curated mappings separate from rebuildable Wikidata claims.
- Use Wikidata as a hub, not as a substitute for provider-specific quirks.

## Safe Use Matrix

| Task                    | Recommended use                                                  | Review trigger                                       |
| ----------------------- | ---------------------------------------------------------------- | ---------------------------------------------------- |
| QID bridge              | Strong when entity type and DOB/name/context agree.              | QID merges, redirects, or has mixed role claims.     |
| External-ID discovery   | Use claims as leads for provider-specific verification.          | Claim would create a second-order bridge.            |
| Player/coach identities | Keep human QID separate from provider player/manager namespaces. | Same person has multiple role-specific IDs.          |
| Team matching           | Use QID plus country/category/team-type context.                 | Men's/women's/youth/reserve ambiguity.               |
| Season/competition      | Use as public context, not the only authority for structure.     | Stage model differs from provider or register model. |

## Do Not Do

- Do not auto-write every Wikidata external ID as an accepted provider bridge.
- Do not treat aliases as identity proof.
- Do not delete or replace published register IDs just because a QID changed.
- Do not ignore deprecated ranks or low-precision dates when using Wikidata as evidence.

## Useful Examples

- [Second-order bridge rejection](../examples/second-order-bridge-rejection.md).
- [Women-only prior beats fuzzy bridge](../examples/women-only-prior-fuzzy-bridge.md).
- [Alias variant duplicate prevention](../examples/alias-variant-duplicate-prevention.md).

## Gotchas

- Claim ranks matter; ignore deprecated claims unless you are auditing history.
- Player-coach identities often have multiple provider IDs for the same person in
  different namespaces.
- Multi-nationality, multiple positions, and career team claims need policy decisions
  before matching.
- Women's football and lower tiers have thinner coverage.
- Some external IDs are slugs or legacy IDs, not stable modern provider IDs.

## References

- [Wikidata](https://www.wikidata.org/)
- [Wikidata Query Service](https://query.wikidata.org/)
- [Wikidata dumps](https://dumps.wikimedia.org/wikidatawiki/entities/)
