---
doc_type: example
content_lane: example
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: examples
stance: illustrative
contribution_model: example_patch
entity_types: [player, team, competition]
matching_fields: [provider_id, entity_type, namespace]
confidence_floor: 1.0
failure_mode: cross_type_provider_id_reuse
decision: [type_gate, review_if_missing_type]
search_tags: [type-gate, provider-id, lookup]
---

# Type-Gated Provider ID Lookup

This example shows why a provider ID lookup must include entity type. A provider's
numeric ID may be unique inside one entity namespace without being globally unique
across every entity type.

## Situation

The register has three accepted bridges:

| entity_id | entity_type | name          | provider     | external_id |
| --------- | ----------- | ------------- | ------------ | ----------- |
| `t_001`   | team        | Riverside FC  | example_data | 8           |
| `c_001`   | competition | Riverside Cup | example_data | 8           |
| `p_001`   | player      | River Stone   | example_data | 44          |

The provider documentation says team IDs and competition IDs are separate namespaces,
even though both are numeric.

## Bad Lookup

```sql
SELECT entity_id
FROM provider_ids
WHERE provider = 'example_data'
  AND external_id = '8';
```

This returns both `t_001` and `c_001`. A caller that takes the first row may attach a
team bridge to a competition or a competition bridge to a team.

## Correct Lookup

```sql
SELECT entity_id
FROM provider_ids
WHERE provider = 'example_data'
  AND external_id = '8'
  AND entity_type = 'team';
```

The type gate is part of the identity claim. It is not an optional filter.

## Write Rule

Before accepting a new bridge:

| Check                                                                  | Required?                                                |
| ---------------------------------------------------------------------- | -------------------------------------------------------- |
| Provider namespace is recognised.                                      | yes                                                      |
| External ID shape is valid for that provider.                          | yes                                                      |
| Entity type is known and matches the provider endpoint.                | yes                                                      |
| Same provider/external ID already exists on a different same-type row. | block                                                    |
| Same provider/external ID exists on a different entity type.           | allowed only when provider docs confirm split namespaces |

## Review Record For Ambiguous Inputs

If the source says only:

```json
{
  "provider": "example_data",
  "external_id": "8",
  "name": "Riverside"
}
```

create a review item:

```text
status: needs_review
reason: missing entity type for provider ID lookup
provider: example_data
external_id: 8
candidate_entities: [t_001, c_001]
```

## Doctrine Demonstrated

- `provider + external_id` is not always enough.
- Provider docs must state whether IDs are globally unique or type-scoped.
- Type gates prevent accidental cross-entity bridge writes.
- A same-provider same-type duplicate is a conflict; a documented cross-type reuse can
  be legitimate.
