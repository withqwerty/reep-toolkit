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
matching_fields: [provider_id, source_snapshot, confidence, matcher_version]
confidence_floor: 0.95
failure_mode: provider_snapshot_drift
decision: [review_drift]
search_tags: [snapshot, drift, refresh]
---

# Snapshot Drift Report

This example shows what to inspect before accepting a provider refresh.

## Previous Snapshot

`provider-players-2026-04-01`

| provider_id | matched_entity | method                 | confidence |
| ----------- | -------------- | ---------------------- | ---------: |
| `100`       | `p_001`        | `bridge:transfermarkt` |      `1.0` |
| `101`       | `p_002`        | `dob+name`             |     `0.95` |
| `102`       | null           | unmatched              |        n/a |

## New Snapshot

`provider-players-2026-04-29`

| provider_id | matched_entity | method                 | confidence |
| ----------- | -------------- | ---------------------- | ---------: |
| `100`       | `p_001`        | `bridge:transfermarkt` |      `1.0` |
| `101`       | `p_777`        | `name+nationality`     |     `0.90` |
| `102`       | `p_003`        | `dob+name`             |     `0.95` |
| `103`       | null           | unmatched              |        n/a |

## Drift Findings

| Finding                                         | Severity | Action                                                         |
| ----------------------------------------------- | -------- | -------------------------------------------------------------- |
| `100` unchanged.                                | low      | no action                                                      |
| `101` changed target and downgraded confidence. | high     | block write; review previous `p_002` mapping before replacing. |
| `102` moved from unmatched to strong match.     | medium   | candidate write if ambiguity checks pass.                      |
| `103` new unmatched residue.                    | low      | track coverage gap.                                            |

## Write Set

Only `102 -> p_003` is eligible for an automatic write. The `101 -> p_777` change is not
a refresh; it is a conflict.

## Reep-Style Lesson

A rerun is not automatically an improvement. Drift reports protect curated mappings from
weaker new evidence and make provider changes visible before they enter public exports.
