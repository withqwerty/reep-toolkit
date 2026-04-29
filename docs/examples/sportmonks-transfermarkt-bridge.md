---
doc_type: example
content_lane: example
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: examples
stance: illustrative
contribution_model: example_patch
provider: sportmonks
entity_types: [player, team]
matching_fields: [sportmonks_id, transfermarkt_id, name, date_of_birth]
confidence_floor: 1.0
failure_mode: direct_bridge_plus_residue
decision: [auto_write, review_residue]
search_tags: [sportmonks, transfermarkt, bridge]
---

# SportMonks Transfermarkt Bridge

This example shows a high-confidence bridge-first ingest. SportMonks records often carry
`transfermarkt_id`, so the matcher should try the Transfermarkt bridge before DOB/name
fallback.

## Source Snapshot

```json
[
  {
    "id": 9001,
    "common_name": "Cole Palmer",
    "date_of_birth": "2002-05-06",
    "transfermarkt_id": "568177"
  },
  {
    "id": 9002,
    "common_name": "Academy Trialist",
    "date_of_birth": null,
    "transfermarkt_id": null
  }
]
```

## Existing Register Evidence

| entity_id | entity_type | name        | date_of_birth | provider      | external_id |
| --------- | ----------- | ----------- | ------------- | ------------- | ----------- |
| `p_001`   | player      | Cole Palmer | 2002-05-06    | transfermarkt | 568177      |

## Matching Decision

| SportMonks ID | Method                 | Outcome                            | Confidence | Why                                                          |
| ------------- | ---------------------- | ---------------------------------- | ---------: | ------------------------------------------------------------ |
| `9001`        | `bridge:transfermarkt` | write SportMonks bridge to `p_001` |      `1.0` | Direct provider-supplied bridge resolves to one live player. |
| `9002`        | none                   | unmatched residue                  |        n/a | No bridge, no DOB, no safe signal path.                      |

## Write

```text
entity_id: p_001
provider: sportmonks
external_id: 9001
source: sportmonks-player-snapshot
confidence: 1.0
method: bridge:transfermarkt
source_snapshot: sportmonks-players-2026-04-29
matcher_version: sportmonks-player-v1
```

## Reep-Style Lesson

Bridge-first matching is not just faster. It reduces the amount of biographical matching
you need to trust. Records without bridges become explicit residue rather than forced
fuzzy matches.
