---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: secondspectrum
entity_types: [player, team, match]
access_tier: paid_or_private
source_kind: living
authority_role: coverage_probe
bridge_providers: []
matching_fields: [match_id, team_metadata, shirt_number, tracking_id]
confidence_floor: 0.0
private_dependencies: []
---

# Second Spectrum

Second Spectrum is a commercial optical-tracking provider under Genius Sports. For
public register work it is reference-only: the provider appears in club and league data
ecosystems, but it does not expose a general public identity bridge.

## Entity Model

| Entity type | Second Spectrum term | ID shape              | Notes                                              |
| ----------- | -------------------- | --------------------- | -------------------------------------------------- |
| Player      | tracking player      | feed/customer key     | Usually resolved through customer roster metadata. |
| Team        | team metadata        | feed/customer key     | Delivery-scoped team context.                      |
| Match       | match                | provider/customer key | Delivery-scoped match key.                         |

## Matching Surface

| Field                 | Use                              | Gotcha                                           |
| --------------------- | -------------------------------- | ------------------------------------------------ |
| Tracking player key   | Customer-local bridge candidate. | Not public and may be delivery-scoped.           |
| Shirt number/position | Relationship evidence.           | Weak without roster metadata.                    |
| Match metadata        | Match context.                   | Confirm date, teams, and competition externally. |

## Reep-Style Linking Advice

- Keep Second Spectrum identifiers provider-scoped.
- Do not publish or infer bridges from tracking rows without roster identity evidence.
- Treat ball/player movement data as analytics output, not identity evidence.

## Gotchas

- No general public sample or Wikidata property.
- Delivery metadata determines whether IDs are match-scoped or customer-stable.
- League contracts and coverage can change independently of ID semantics.

## References

- [Second Spectrum](https://www.secondspectrum.com/)
- [Genius Sports](https://www.geniussports.com/)
- [kloppy](https://github.com/PySport/kloppy)
