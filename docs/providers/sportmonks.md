---
doc_type: provider_card
content_lane: reference
status: review_ready
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: sportmonks
entity_types: [player, team, coach, competition, season, match]
access_tier: paid_or_private
source_kind: living
authority_role: metadata_source
bridge_providers: [transfermarkt]
matching_fields:
  [
    sportmonks_id,
    transfermarkt_id,
    name,
    date_of_birth,
    nationality_id,
    country_id,
    fixture_id,
  ]
confidence_floor: 1.0
private_dependencies: []
---

# SportMonks

SportMonks is a commercial football API with broad entity coverage and one unusually
valuable identity feature: many player and team records carry a Transfermarkt ID.

## Why It Matters Before You Start

SportMonks can be much easier to link than signal-only providers because its
`transfermarkt_id` often gives a direct path into an existing register. The fallback
path still matters because bridge coverage is not universal.

## Entity Model

| Register type | SportMonks term | ID shape | Notes                                              |
| ------------- | --------------- | -------- | -------------------------------------------------- |
| Player        | player          | numeric  | Often carries `transfermarkt_id`.                  |
| Team          | team            | numeric  | Often carries `transfermarkt_id`.                  |
| Coach         | coach           | numeric  | Coach bridges vary by plan/coverage.               |
| Competition   | league          | numeric  | SportMonks "league" is usually competition family. |
| Season        | season          | numeric  | First-class API entity.                            |
| Match         | fixture         | numeric  | First-class API entity.                            |

## Matching Surface

| Field                | Use                         | Gotcha                                                           |
| -------------------- | --------------------------- | ---------------------------------------------------------------- |
| `transfermarkt_id`   | Strong player/team bridge.  | Missing for some records; do not assume universal coverage.      |
| Player name fields   | Fallback matching.          | Prefer full/common names over abbreviated display names.         |
| `date_of_birth`      | Strong player/coach signal. | Check nulls and format.                                          |
| `nationality_id`     | Corroboration.              | Foreign key; resolve country table before comparing.             |
| `position_id`        | Weak corroboration.         | Foreign key; resolve lookup table before comparing labels.       |
| Fixture participants | Match matching.             | Home/away semantics and participant arrays need careful parsing. |

## Bridge Surface

| Bridge route                             | Use                                           | Caution                                                         |
| ---------------------------------------- | --------------------------------------------- | --------------------------------------------------------------- |
| SportMonks player → Transfermarkt        | Primary direct player bridge.                 | Present for many active players, not all academy/youth records. |
| SportMonks team → Transfermarkt          | Primary direct team bridge.                   | Check category, country, and men's/women's/youth scope.         |
| SportMonks coach → Transfermarkt manager | Strong where present.                         | Coach coverage varies by plan and endpoint.                     |
| SportMonks fallback → register           | DOB + normalised name + resolved nationality. | Review null-DOB and same-name collisions.                       |

## Reep-Style Linking Advice

- Bridge through Transfermarkt first when the field is present.
- Fall back to DOB plus normalised name for players without bridges.
- Resolve foreign keys before comparing nationality, position, or country.
- Treat stale API versions or cached old data as a different source snapshot.
- Do not let a missing bridge force a mint; unmatched SportMonks records can wait for
  corroboration.

## Safe Use Matrix

| Task           | Recommended use                                                  | Review trigger                                       |
| -------------- | ---------------------------------------------------------------- | ---------------------------------------------------- |
| Player bridge  | Direct `transfermarkt_id`, or DOB plus normalised-name fallback. | Fuzzy id-finder row conflicts with stronger priors.  |
| Team bridge    | Direct `transfermarkt_id` plus category/country context.         | Men's/women's/youth/reserve ambiguity.               |
| Season bridge  | Map `season_id` and `stage_id` to the right register level.      | Split-season or stage model mismatch.                |
| Match bridge   | Fixture ID plus resolved home/away participants.                 | Participant array lacks role semantics.              |
| Classification | Use structured IDs after resolving lookup tables.                | Derived classification conflicts with source priors. |

## Do Not Do

- Do not let id-finder matches override women-only priors.
- Do not flatten stages into parent seasons.
- Do not treat missing `transfermarkt_id` as permission to mint.
- Do not compare country, nationality, or position IDs before resolving their lookup
  tables.

## Useful Examples

- [SportMonks Transfermarkt bridge](../examples/sportmonks-transfermarkt-bridge.md).
- [SportMonks stage and season mismatch](../examples/sportmonks-stage-season-mismatch.md).
- [Women-only prior beats fuzzy bridge](../examples/women-only-prior-fuzzy-bridge.md).

## Gotchas

- API includes and nested relationships can affect quota and payload shape.
- Country and position values are IDs, not labels.
- Match feeds may expose abbreviated display names; use common/full names for identity
  matching when the endpoint supplies them.
- Fixture participants need explicit home/away handling.
- Historical API versions may contain duplicate or inactive records that should be
  rematched from current snapshots.
- Missing `transfermarkt_id` is a review/backlog signal, not a reason to mint a new
  entity by name alone.

## References

- [SportMonks](https://www.sportmonks.com/)
- [SportMonks football docs](https://docs.sportmonks.com/football/)
- [Transfermarkt](transfermarkt.md)
