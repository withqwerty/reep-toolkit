---
doc_type: example
content_lane: example
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: examples
stance: illustrative
contribution_model: example_patch
entity_types: [player]
matching_fields: [provider_id, date_of_birth, name, source_snapshot, confidence]
confidence_floor: 0.95
failure_mode: same_provider_bridge_conflict
decision: [review]
search_tags: [bridge-conflict, same-provider, review]
---

# Bridge Conflict Case Study

This case shows what happens when a new source proposes a bridge that disagrees with
stronger existing evidence.

## Situation

The register already has a player entity with a strong Transfermarkt bridge.

| entity_id | name        | date_of_birth | provider      | external_id | method         | confidence |
| --------- | ----------- | ------------- | ------------- | ----------- | -------------- | ---------: |
| `p_001`   | Cole Palmer | 2002-05-06    | transfermarkt | 568177      | wikidata:P2446 |        1.0 |
| `p_001`   | Cole Palmer | 2002-05-06    | wikidata      | Q123        | seed           |        1.0 |

A new community bridge snapshot claims that the same source player maps to a different
Transfermarkt ID.

```json
{
  "source_provider": "community_fbref_tm_map",
  "source_snapshot": "community-fbref-tm-2026-04-29",
  "fbref_id": "dc7f8a28",
  "name": "Cole Palmer",
  "date_of_birth": "2002-05-06",
  "transfermarkt_id": "999999"
}
```

The registry also has a different live entity with that proposed Transfermarkt ID:

| entity_id | name         | date_of_birth | provider      | external_id |
| --------- | ------------ | ------------- | ------------- | ----------- |
| `p_777`   | Cole Example | 2002-05-06    | transfermarkt | 999999      |

## Naive Write

A naive matcher might write:

```text
p_001 -> transfermarkt:999999
```

That would make one entity carry two Transfermarkt player IDs and would also make the
same Transfermarkt ID point at two live entities.

## Correct Routing

The new bridge is not an update. It is a conflict.

| Check                                                             | Result                       | Consequence                |
| ----------------------------------------------------------------- | ---------------------------- | -------------------------- |
| Does `transfermarkt:999999` already exist?                        | yes, on `p_777`              | block auto-write           |
| Does `p_001` already have a stronger Transfermarkt bridge?        | yes, `568177` at 1.0         | preserve existing bridge   |
| Does biographical evidence distinguish `p_001` and `p_777`?       | no, same DOB in this example | route to review            |
| Can the community mapping overwrite Wikidata-derived TM evidence? | no                           | keep as candidate evidence |

## Review Record

```text
review_type: bridge_conflict
provider: transfermarkt
proposed_external_id: 999999
proposed_entity_id: p_001
current_entity_for_external_id: p_777
existing_bridge_on_proposed_entity: transfermarkt:568177
source_snapshot: community-fbref-tm-2026-04-29
method: derived-community-bridge
confidence: 0.90
decision: needs_review
```

## Possible Reviewer Outcomes

| Reviewer finding                         | Action                                                            |
| ---------------------------------------- | ----------------------------------------------------------------- |
| Community map is wrong.                  | Reject candidate and keep rejection history.                      |
| `p_001` and `p_777` are duplicates.      | Start duplicate resolution; do not write the bridge in isolation. |
| Transfermarkt retired/reassigned one ID. | Preserve history, update bridge state, and document source drift. |
| Existing register bridge is wrong.       | Correct with audit trail, not silent overwrite.                   |

## Write Set

No automatic write.

The only safe write is the review candidate:

```text
candidate_bridge:
  entity_id: p_001
  provider: transfermarkt
  external_id: 999999
  confidence: 0.90
  method: derived-community-bridge
  review_status: needs_review
```

## Doctrine Demonstrated

- Strong existing bridges are not overwritten by weaker derived evidence.
- Same-provider conflicts are duplicate-resolution work, not normal bridge writes.
- A changed target is a review event, not a refresh improvement.
- Rejected candidates should be stored so the same bad bridge does not return on every
  rerun.
