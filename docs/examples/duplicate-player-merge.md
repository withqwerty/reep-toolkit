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
matching_fields: [provider_id, alias, date_of_birth, source_snapshot]
confidence_floor: 0.95
failure_mode: duplicate_player
decision: [tombstone, redirect, move_non_conflicts]
search_tags: [duplicate, merge, tombstone]
---

# Duplicate Player Merge

This example shows the merge policy from
[duplicate resolution](../guides/duplicate-resolution.md) with concrete rows.

## Before

Two live entities represent the same player.

| entity_id | name           | date_of_birth | status |
| --------- | -------------- | ------------- | ------ |
| `p_001`   | Cole Palmer    | 2002-05-06    | live   |
| `p_999`   | Cole J. Palmer | 2002-05-06    | live   |

Provider bridges:

| entity_id | provider      | external_id | method           |
| --------- | ------------- | ----------- | ---------------- |
| `p_001`   | transfermarkt | 568177      | wikidata-bridge  |
| `p_001`   | wikidata      | Q123        | seed             |
| `p_999`   | fotmob        | 292462      | dob+name         |
| `p_999`   | thesportsdb   | 34146086    | wikipedia-bridge |

No same-provider conflict exists.

## Decision

`p_001` remains canonical because it has the stronger older bridge set. `p_999` becomes
a redirect.

```text
p_999.deleted_at = 2026-04-29T00:00:00Z
p_999.canonical_entity_id = p_001
```

## Data Movement

Move non-conflicting bridges:

| provider    | external_id | from    | to      |
| ----------- | ----------- | ------- | ------- |
| fotmob      | 292462      | `p_999` | `p_001` |
| thesportsdb | 34146086    | `p_999` | `p_001` |

Move aliases:

| alias          | from    | to      |
| -------------- | ------- | ------- |
| Cole J. Palmer | `p_999` | `p_001` |

## After

| entity_id | status     | canonical_entity_id |
| --------- | ---------- | ------------------- |
| `p_001`   | live       | null                |
| `p_999`   | tombstoned | `p_001`             |

## Merge Audit

```text
retired_entity_id: p_999
canonical_entity_id: p_001
reason: duplicate_player
evidence: same DOB, name alias, non-conflicting provider bridges
moved_bridges: 2
conflicts_left: 0
```

## Reep-Style Lesson

The retired ID keeps resolving. The data moves where safe. Conflicts would stay behind
for review rather than being flattened into the canonical entity.
