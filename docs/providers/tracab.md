---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: tracab
entity_types: [player, team, match]
access_tier: paid_or_private
source_kind: living
authority_role: coverage_probe
bridge_providers: []
matching_fields: [match_id, team_metadata, shirt_number, tracking_id]
confidence_floor: 0.0
private_dependencies: []
---

# TRACAB

TRACAB is a commercial optical-tracking provider. It matters to identity-resolution work
because clubs and leagues may see TRACAB identifiers in tracking deliveries, but there
is no public bridge surface.

## Entity Model

| Entity type | TRACAB term     | ID shape              | Notes                                              |
| ----------- | --------------- | --------------------- | -------------------------------------------------- |
| Player      | tracking player | feed/customer key     | Usually resolved through customer roster metadata. |
| Team        | team metadata   | feed/customer key     | Match-delivery context.                            |
| Match       | match           | provider/customer key | Delivery-scoped match key.                         |

## Matching Surface

| Field               | Use                              | Gotcha                                      |
| ------------------- | -------------------------------- | ------------------------------------------- |
| Tracking player key | Customer-local bridge candidate. | Not public and may be match-scoped.         |
| Shirt number        | Relationship evidence.           | Never person identity proof by itself.      |
| Team metadata       | Context.                         | Depends on customer roster setup.           |
| Match metadata      | Match context.                   | Confirm against a canonical fixture source. |

## Reep-Style Linking Advice

- Treat TRACAB as reference-only unless you have customer metadata.
- Do not infer public player or team IDs from tracking identifiers.
- Preserve match-delivery provenance if commercial IDs are ever bridged.

## Gotchas

- No public sample or Wikidata property provides a general bridge.
- Tracking IDs and roster metadata are usually customer-maintained.
- Coordinate and format details are parser concerns, not identity proof.

## References

- [TRACAB](https://www.tracab.com/)
- [EA Sports TRACAB announcement](https://www.ea.com/tracab/news/ea-sports-realism-technology)
- [kloppy](https://github.com/PySport/kloppy)
