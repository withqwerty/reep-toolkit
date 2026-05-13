---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: signality
entity_types: [player, team, match]
access_tier: paid_or_private
source_kind: living
authority_role: coverage_probe
bridge_providers: []
matching_fields: [match_id, team_metadata, tracking_id, venue]
confidence_floor: 0.0
private_dependencies: []
---

# Signality

Signality is a commercial optical-tracking provider in the Spiideo ecosystem. It is
useful catalogue context for tracking data, but it does not expose a public
identity-resolution surface.

## Entity Model

| Entity type | Signality term  | ID shape              | Notes                                             |
| ----------- | --------------- | --------------------- | ------------------------------------------------- |
| Player      | tracking player | feed/customer key     | Resolved through delivery metadata where present. |
| Team        | team metadata   | feed/customer key     | Delivery-scoped team context.                     |
| Match       | match           | provider/customer key | Delivery-scoped match key.                        |
| Venue       | venue           | metadata key          | Context only.                                     |

## Matching Surface

| Field               | Use                       | Gotcha                                             |
| ------------------- | ------------------------- | -------------------------------------------------- |
| Tracking key        | Customer-local candidate. | Not a public bridge.                               |
| Venue/team metadata | Context.                  | Useful for delivery audit, not identity by itself. |
| Match metadata      | Match context.            | Confirm against a canonical fixture source.        |

## Reep-Style Linking Advice

- Treat Signality as reference-only unless roster metadata is available.
- Keep venue, team, and tracking keys in separate namespaces.
- Use tracking rows as relationship context, not person identity proof.

## Gotchas

- No public identity bridge or general sample dataset.
- Tracking data and video workflow metadata can be delivered together; keep identity
  claims separate from format claims.

## References

- [Signality](https://www.signality.com/)
- [Spiideo](https://www.spiideo.com/)
- [kloppy](https://github.com/PySport/kloppy)
