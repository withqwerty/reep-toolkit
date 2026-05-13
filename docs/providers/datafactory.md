---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: datafactory
entity_types: [player, team, competition, season, match]
access_tier: paid_or_private
source_kind: living
authority_role: coverage_probe
bridge_providers: []
matching_fields: [datafactory_id, name, team_id, match_id, competition_id]
confidence_floor: 0.95
private_dependencies: []
---

# DataFactory

DataFactory is a Latin American sports-data provider with strong regional coverage. For
a public register, it is mostly ecosystem context unless a subscriber feed supplies
typed player, team, and match identifiers with enough metadata to pass normal gates.

## Entity Model

| Entity type | DataFactory term | ID shape         | Notes                                 |
| ----------- | ---------------- | ---------------- | ------------------------------------- |
| Player      | player           | provider key     | Subscriber metadata only.             |
| Team        | team             | provider key     | Regional competition context matters. |
| Match       | match            | provider key     | Feed-scoped match key.                |
| Competition | competition      | provider key     | Feed-scoped competition key.          |
| Event       | event            | match-scoped key | Event IDs are not entity bridges.     |

## Matching Surface

| Field              | Use                        | Gotcha                                        |
| ------------------ | -------------------------- | --------------------------------------------- |
| Player/team IDs    | Provider bridge candidate. | No public cross-provider bridge.              |
| Names              | Candidate signal.          | Spanish/Portuguese labels need normalisation. |
| Match ID and teams | Match candidate.           | Confirm against a canonical fixture source.   |
| Event IDs          | Analytics context.         | Match-scoped, not register entity identity.   |

## Reep-Style Linking Advice

- Treat DataFactory IDs as paid-feed provider namespaces.
- Use it for regional coverage context where Opta or StatsBomb coverage is thinner.
- Do not accept name-only person bridges.
- Keep event identifiers out of the entity bridge layer.

## Gotchas

- Public documentation of ID semantics is limited.
- Regional labels and names need language-aware normalisation.
- Commercial coverage does not imply public reproducibility.

## References

- [DataFactory](https://www.datafactory.la/)
- [kloppy](https://github.com/PySport/kloppy)
