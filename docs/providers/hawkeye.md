---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: hawkeye
entity_types: [player, team, match]
access_tier: paid_or_private
source_kind: living
authority_role: coverage_probe
bridge_providers: []
matching_fields: [match_id, team_metadata, tracking_id]
confidence_floor: 0.0
private_dependencies: []
---

# Hawk-Eye

Hawk-Eye is a Sony-owned officiating and tracking technology provider. In football, its
goal-line and officiating footprint is much more visible than any public entity-ID
surface.

## Entity Model

| Entity type | Hawk-Eye term   | ID shape              | Notes                                             |
| ----------- | --------------- | --------------------- | ------------------------------------------------- |
| Player      | tracking player | feed/customer key     | Resolved through customer metadata where present. |
| Team        | team metadata   | feed/customer key     | Delivery-scoped team context.                     |
| Match       | match           | provider/customer key | Delivery-scoped match key.                        |

## Matching Surface

| Field                  | Use                       | Gotcha                                                           |
| ---------------------- | ------------------------- | ---------------------------------------------------------------- |
| Tracking key           | Customer-local candidate. | Not a public bridge.                                             |
| Team/match metadata    | Context.                  | Depends on delivery configuration.                               |
| Officiating deployment | Ecosystem context.        | Goal-line technology presence does not imply player-ID coverage. |

## Reep-Style Linking Advice

- Treat Hawk-Eye as ecosystem context unless a real delivery includes roster metadata.
- Do not infer player or team identity from goal-line/officiating deployment.
- Keep tracking and officiating concepts separate in provider documentation.

## Gotchas

- No general public identity surface.
- Goal-line coverage and tracking coverage are different questions.
- Customer metadata, not public provider pages, resolves identities.

## References

- [Hawk-Eye Innovations](https://www.hawkeyeinnovations.com/)
- [kloppy](https://github.com/PySport/kloppy)
