---
doc_type: example
content_lane: example
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: examples
stance: illustrative
contribution_model: example_patch
entity_types: [player, coach]
matching_fields: [provider_id, name, date_of_birth, gender, source_authority]
confidence_floor: 0.95
failure_mode: source_authority_conflict
decision: [candidate_only, review]
search_tags: [women-only-prior, fuzzy-bridge, authority]
---

# Women-Only Prior Beats Fuzzy Bridge

This example shows why a confidence score does not outrank source authority. A fuzzy
provider bridge should not override an existing women-only context without stronger
identity evidence.

## Situation

The register has a player entity with women-only provider evidence:

| entity_id | name          | date_of_birth | provider    | external_id | context    |
| --------- | ------------- | ------------- | ----------- | ----------- | ---------- |
| `p_001`   | Silvia Romano | 1989-05-12    | soccerdonna | sd_1001     | women-only |
| `p_001`   | Silvia Romano | 1989-05-12    | wikidata    | Q1001       | female     |

A broad provider id-finder snapshot proposes:

```json
{
  "provider": "sportmonks",
  "source_snapshot": "sportmonks-idfinder-2026-04-29",
  "external_id": "sm_9001",
  "name": "Silvio Romano",
  "date_of_birth": "1989-05-12",
  "gender": "male",
  "method": "dob-name-alt",
  "confidence": 0.95
}
```

The DOB matches and the name is close, but the proposed row conflicts with existing
women-only evidence.

## Bad Write

```text
p_001 -> sportmonks:sm_9001
confidence: 0.95
method: dob-name-alt
```

This makes the fuzzy source an identity anchor and can pollute classification fields
downstream.

## Correct Routing

Treat the provider row as a candidate, not an accepted bridge:

| Check                                                 | Result                 | Consequence            |
| ----------------------------------------------------- | ---------------------- | ---------------------- |
| Existing women-only provider evidence                 | yes                    | require stronger proof |
| Proposed source method                                | fuzzy DOB/name variant | not enough             |
| Proposed classification conflicts with existing prior | yes                    | block auto-write       |
| Direct provider ID corroboration                      | no                     | route to review        |
| Independent target-provider page confirms same person | not fetched            | keep as candidate      |

## Review Record

```text
review_type: authority_conflict
entity_id: p_001
existing_prior: women-only-provider
proposed_provider: sportmonks
proposed_external_id: sm_9001
proposed_gender: male
method: dob-name-alt
confidence: 0.95
decision: needs_direct_corroboration
```

## Promotion Conditions

The candidate can be promoted only if stronger evidence appears:

- the target provider page confirms the same person and entity type,
- another independent source bridges the same provider ID,
- the name discrepancy is explained by a documented alias,
- the conflicting classification is proven to be a provider error.

## Doctrine Demonstrated

- Confidence is not the same thing as authority.
- Women-only provider evidence is a strong prior.
- Fuzzy id-finder rows are hints, not identity anchors.
- Classification conflicts should preserve both pieces of evidence until reviewed.
