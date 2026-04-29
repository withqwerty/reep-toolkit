---
doc_type: example
content_lane: example
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: examples
stance: illustrative
contribution_model: example_patch
entity_types: [player, team]
matching_fields: [wikidata, provider_id, derivation_rule, source_snapshot]
confidence_floor: 0.95
failure_mode: second_order_hub_bridge
decision: [candidate_only]
search_tags: [wikidata, second-order, bridge]
---

# Second-Order Bridge Rejection

This example shows why a bridge discovered through a hub source should not be written
automatically unless the hub relationship is current, typed, and corroborated.

## Situation

The register has a team:

| entity_id | entity_type | name         | provider | external_id |
| --------- | ----------- | ------------ | -------- | ----------- |
| `t_001`   | team        | North United | wikidata | Q5001       |

A Wikidata-derived extraction claims:

```json
{
  "source_provider": "wikidata",
  "source_snapshot": "wikidata-football-2026-04-29",
  "subject_qid": "Q5001",
  "property": "P12345",
  "claimed_provider": "example_stats",
  "claimed_external_id": "nu-1994"
}
```

The property appears to point to an `example_stats` team page.

## Bad Write

```text
t_001 -> example_stats:nu-1994
confidence: 1.0
method: wikidata-derived
```

This treats a second-order statement as if the target provider itself confirmed the
bridge.

## Required Checks

| Check                                                | Result in this case | Consequence                 |
| ---------------------------------------------------- | ------------------- | --------------------------- |
| Does `example_stats:nu-1994` resolve to a live page? | unknown             | cannot auto-write           |
| Is the page definitely a team page?                  | unknown             | cannot auto-write           |
| Is the source property current and not deprecated?   | unknown             | cannot auto-write           |
| Does another provider corroborate it?                | no                  | keep as candidate           |
| Does the provider ID collide with another team?      | not checked         | must check before any write |

## Correct Routing

Store candidate evidence, not an accepted bridge:

```text
review_type: second_order_bridge
entity_id: t_001
hub_provider: wikidata
hub_id: Q5001
claimed_provider: example_stats
claimed_external_id: nu-1994
confidence: 0.90
review_status: needs_provider_confirmation
source_snapshot: wikidata-football-2026-04-29
```

## Promotion Conditions

Promote the candidate only when one of these is true:

- the target provider page is fetched and proves the same entity type,
- a second independent source confirms the same provider ID,
- the hub property is known to be type-specific, stable, current, and reviewed,
- an existing accepted provider bridge leads to the same target.

## Rejection Conditions

Reject the candidate if:

- the target provider page is gone,
- the page is for the wrong entity type,
- the external ID belongs to a different live entity,
- the hub statement is deprecated or stale,
- the bridge depends on a broad search result rather than a typed external ID claim.

## Doctrine Demonstrated

- Hub sources are evidence, not automatic authority.
- Second-order bridges need stricter lineage than direct provider bridges.
- Whitelisting a provider does not make every derived bridge safe.
- Candidate storage prevents repeated rediscovery without corrupting accepted mappings.
