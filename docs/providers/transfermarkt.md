---
doc_type: provider_card
content_lane: reference
status: review_ready
public_safe: true
last_verified: 2026-04-29
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: transfermarkt
entity_types: [player, team, coach, competition, season, match]
access_tier: public_grey
source_kind: living
authority_role: bridge_spine
bridge_providers: [wikidata, sportmonks, fbref, fpl]
matching_fields:
  [
    transfermarkt_id,
    name,
    date_of_birth,
    nationality,
    country,
    position,
    competition_code,
  ]
confidence_floor: 1.0
private_dependencies: []
---

# Transfermarkt

Transfermarkt is the de facto football bridge target. Even when a project does not use
Transfermarkt directly, other providers and Wikidata often use Transfermarkt IDs as
their common join point.

## Why It Matters Before You Start

Transfermarkt IDs are everywhere: Wikidata, public bridge datasets, fan tools, and many
football analytics projects. A register that can resolve Transfermarkt well can often
resolve many other providers indirectly.

The trap is that Transfermarkt is not one namespace. Players, managers, clubs,
competitions, and matches have different URL families and sometimes separate ID spaces.

## Entity Model

| Entity type | Transfermarkt term          | ID shape   | Notes                                                                               |
| ----------- | --------------------------- | ---------- | ----------------------------------------------------------------------------------- |
| Player      | player / Spieler            | numeric    | Stable player profile ID.                                                           |
| Coach       | manager / Trainer           | numeric    | Separate from player ID, even for the same human.                                   |
| Team        | club / Verein               | numeric    | Senior clubs, with country usually derived through competition context in datasets. |
| Competition | Wettbewerb                  | short code | Codes are not ISO country codes.                                                    |
| Season      | query parameter             | year-like  | Usually not a first-class entity ID.                                                |
| Match       | match report / Spielbericht | numeric    | Useful fixture bridge where available.                                              |

## Matching Surface

| Field            | Use                         | Gotcha                                                          |
| ---------------- | --------------------------- | --------------------------------------------------------------- |
| Transfermarkt ID | Strong bridge.              | Carry entity type; player and manager IDs are different spaces. |
| Name             | Display and alias evidence. | URL slugs may be transliterated; page names keep accents.       |
| Date of birth    | Strong player/coach signal. | Profile formats are day-first in European style.                |
| Nationality      | Corroboration.              | Multiple citizenships are common.                               |
| Club/team ID     | Team context.               | Loans and current-club fields are point-in-time.                |
| Competition code | Competition bridge.         | Codes like `GB1`, `KOR1`, `CLI` are provider-specific.          |

## Reep-Style Linking Advice

- Treat a verified Transfermarkt bridge as high-confidence identity evidence.
- Keep player and manager IDs as separate provider namespaces or separate
  entity-type-scoped rows.
- Use DOB plus normalised name to link player and coach identities for the same human
  when needed.
- Do not infer country directly from club name; use competition or dataset-provided
  country context.

## Safe Use Matrix

| Task               | Recommended use                                                      | Review trigger                                       |
| ------------------ | -------------------------------------------------------------------- | ---------------------------------------------------- |
| Player bridge      | Direct numeric player ID, or DOB plus strong provider corroboration. | Same ID on another live player.                      |
| Coach bridge       | Manager/trainer namespace, not player namespace.                     | Same human has both player and manager profiles.     |
| Team bridge        | Club ID plus country or competition context.                         | Name-only match, reserve/youth/women ambiguity.      |
| Competition bridge | Provider competition code with documented level and country.         | Code reused, renamed, or ambiguous across countries. |
| Season bridge      | Scoped to competition plus year.                                     | Bare year used as if it were globally unique.        |
| Match bridge       | Match-report ID where teams/date are consistent.                     | Team bridge missing or fixture moved/abandoned.      |

## Do Not Do

- Do not treat player IDs and manager IDs as one global human namespace.
- Do not treat a season year as a standalone season bridge.
- Do not strip semantic club-name prefixes such as `Real` or `Sporting` before checking
  for collisions.
- Do not let a Transfermarkt-derived bridge overwrite stronger curated evidence without
  review.

## Useful Examples

- [Structural season ID collision](../examples/structural-season-id-collision.md).
- [Semantic team prefix collision](../examples/semantic-team-prefix-collision.md).
- [Fixture-overlap team bridge](../examples/fixture-overlap-team-bridge.md).

## Gotchas

- Player-coach duplication is normal: one human can have a player profile and a manager
  profile.
- Competition codes are provider conventions, not ISO codes.
- Height and dates use European display formats on pages.
- Current team is a moving field, especially during loans and transfer windows.
- Academy and lower-tier players may have incomplete biographical fields.

## References

- [Transfermarkt](https://www.transfermarkt.com/)
- [Wikidata P2446](https://www.wikidata.org/wiki/Property:P2446),
  [P2447](https://www.wikidata.org/wiki/Property:P2447),
  [P7223](https://www.wikidata.org/wiki/Property:P7223),
  [P12758](https://www.wikidata.org/wiki/Property:P12758)
- [dcaribou/transfermarkt-datasets](https://github.com/dcaribou/transfermarkt-datasets)
- [worldfootballR_data](https://github.com/JaseZiv/worldfootballR_data)
