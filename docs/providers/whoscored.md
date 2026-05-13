---
doc_type: provider_card
content_lane: reference
status: review_ready
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: whoscored
entity_types: [player, team, coach, competition, season, stage, match]
access_tier: public_grey
source_kind: living
authority_role: corroborator
bridge_providers: [opta]
matching_fields:
  [whoscored_id, name, country, region_id, tournament_id, season_id, stage_id, match_id]
confidence_floor: 0.95
private_dependencies: []
---

# WhoScored

WhoScored is a football statistics site whose public surface uses its own numeric IDs
for regions, tournaments, seasons, stages, teams, players, and matches. It licences
Opta-style event data, but it does not expose a public Opta bridge.

## Why It Matters Before You Start

WhoScored is useful for competition and match coverage, but it is easy to over-trust
because the underlying event provider is familiar. Treat WhoScored IDs as WhoScored
provider IDs. Do not infer an Opta UUID or Opta numeric bridge from a WhoScored row.

## Entity Model

| Entity type | WhoScored term | ID shape              | Notes                                 |
| ----------- | -------------- | --------------------- | ------------------------------------- |
| Player      | player         | numeric               | Mostly profile/stat surface.          |
| Team        | team           | numeric               | Team IDs are provider-scoped.         |
| Coach       | coach          | numeric where present | Coverage is partial.                  |
| Region      | region         | numeric               | Country/area grouping; not ISO.       |
| Competition | tournament     | numeric               | Region-scoped in URLs and metadata.   |
| Season      | season         | numeric               | Tournament-scoped.                    |
| Stage       | stage          | numeric               | Season substructure.                  |
| Match       | match          | numeric               | Stable match key in provider context. |

## Matching Surface

| Field                         | Use                     | Gotcha                                            |
| ----------------------------- | ----------------------- | ------------------------------------------------- |
| `region_id` + `tournament_id` | Competition candidate.  | Tournament names repeat across countries.         |
| `season_id` + `stage_id`      | Structural context.     | Do not flatten stage into season without mapping. |
| `match_id`                    | Match bridge candidate. | Resolve teams/date/competition before accepting.  |
| Team IDs and names            | Match/team context.     | Region and tournament context matter.             |
| Player name/team/position     | Weak person candidate.  | No public deterministic Opta bridge.              |

## Bridge Surface

| Bridge route                                 | Use                                                           | Caution                                  |
| -------------------------------------------- | ------------------------------------------------------------- | ---------------------------------------- |
| WhoScored competition → register competition | Country-aware normalised name plus region/tournament context. | Never match tournament name alone.       |
| WhoScored match → register match             | Match ID plus date, teams, season, and stage.                 | Stage/round modelling can differ.        |
| WhoScored player → register person           | DOB/name only if a trusted profile source supplies DOB.       | Name/team/position alone is review-only. |
| WhoScored → Opta                             | Internal/commercial relationship only.                        | Not public bridge evidence.              |

## Reep-Style Linking Advice

- Store WhoScored as its own provider namespace.
- For competitions, match `(region, normalised_name)` rather than name alone.
- Preserve season and stage IDs separately; they are useful structural evidence.
- Treat player rows as candidates unless there is explicit person evidence.
- Use WhoScored match structure to narrow candidates, not as a source of Opta IDs.

## Gotchas

- Region IDs are provider-specific and not ISO country codes.
- Tournament names can drift by season and can repeat across countries.
- Stage IDs are provider structure, not automatically your public stage ontology.
- Position labels are event/stat-site labels and may not round-trip to Opta or Wyscout.
- The apparent Opta relationship is not a public bridge.

## References

- [WhoScored](https://www.whoscored.com/)
- [FairPlay Sports Media](https://www.fairplaysportsmedia.com/)
- [Opta / Stats Perform](opta.md)
