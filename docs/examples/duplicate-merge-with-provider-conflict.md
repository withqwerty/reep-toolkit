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
failure_mode: duplicate_with_provider_conflict
decision: [tombstone, preserve_conflict]
search_tags: [duplicate, merge, provider-conflict]
---

# Duplicate Merge With Provider Conflict

This case extends [duplicate player merge](duplicate-player-merge.md). The two entities
are likely the same real player, but they have conflicting same-provider IDs. That
blocks automatic bridge movement.

## Before

| entity_id | name             | date_of_birth | status |
| --------- | ---------------- | ------------- | ------ |
| `p_001`   | Alex Rivera      | 1998-03-14    | live   |
| `p_888`   | Alejandro Rivera | 1998-03-14    | live   |

Evidence suggests they are the same person:

- same date of birth,
- compatible names,
- same nationality,
- same historical club context,
- one provider aliases `Alex` and `Alejandro`.

Provider bridges:

| entity_id | provider      | external_id      | method                      | confidence |
| --------- | ------------- | ---------------- | --------------------------- | ---------: |
| `p_001`   | wikidata      | Q111             | seed                        |        1.0 |
| `p_001`   | transfermarkt | 1111             | wikidata:P2446              |        1.0 |
| `p_001`   | fotmob        | 2222             | dob+name                    |       0.95 |
| `p_888`   | transfermarkt | 9999             | sportmonks:transfermarkt_id |        1.0 |
| `p_888`   | sportmonks    | 3333             | bridge:transfermarkt        |        1.0 |
| `p_888`   | alias         | Alejandro Rivera | provider-alias              |        n/a |

## The Tempting Bad Merge

The wrong merge moves every row from `p_888` to `p_001`:

```text
p_001 -> transfermarkt:1111
p_001 -> transfermarkt:9999
```

That leaves one live player with two Transfermarkt player IDs. It hides the conflict
inside the canonical entity.

## Correct Merge Plan

The duplicate can still be tombstoned, but conflicting bridges do not move
automatically.

```text
p_001 remains canonical
p_888 is tombstoned
p_888.canonical_entity_id = p_001
```

## Data Movement

| Row                      | Action                                                                  | Reason                                            |
| ------------------------ | ----------------------------------------------------------------------- | ------------------------------------------------- |
| `sportmonks:3333`        | move to `p_001` only if it depends on accepted `transfermarkt:9999`? no | Its bridge path depends on the disputed TM ID.    |
| `transfermarkt:9999`     | do not move                                                             | Same-provider conflict with `transfermarkt:1111`. |
| alias `Alejandro Rivera` | move                                                                    | Alias is non-conflicting and helps search.        |
| merge audit              | write                                                                   | Required for reversibility.                       |

## Conflict Review Record

```text
review_type: merge_conflict
canonical_entity_id: p_001
retired_entity_id: p_888
provider: transfermarkt
canonical_external_id: 1111
retired_external_id: 9999
evidence_summary: same DOB and alias match, but conflicting Transfermarkt IDs
decision: unresolved
```

## After

| entity_id | status     | canonical_entity_id |
| --------- | ---------- | ------------------- |
| `p_001`   | live       | null                |
| `p_888`   | tombstoned | `p_001`             |

Canonical bridges:

| entity_id | provider      | external_id | state    |
| --------- | ------------- | ----------- | -------- |
| `p_001`   | wikidata      | Q111        | accepted |
| `p_001`   | transfermarkt | 1111        | accepted |
| `p_001`   | fotmob        | 2222        | accepted |

Conflict rows:

| provider      | external_id | original_entity | review_status                     |
| ------------- | ----------- | --------------- | --------------------------------- |
| transfermarkt | 9999        | `p_888`         | unresolved                        |
| sportmonks    | 3333        | `p_888`         | blocked_by_transfermarkt_conflict |

## When the Conflict Resolves

If a reviewer proves `transfermarkt:9999` is the same real player:

1. mark `transfermarkt:9999` as accepted alias/retired provider ID if the register
   permits multiple historical IDs,
2. move or relink dependent `sportmonks:3333`,
3. record the evidence that explains why two same-provider IDs are valid.

If a reviewer proves `transfermarkt:9999` is a different player:

1. split the bad duplicate merge,
2. restore `p_888` or create the right canonical target,
3. retain the failed merge audit so the same merge is not repeated.

## Doctrine Demonstrated

- Tombstoning a duplicate does not mean flattening every row into the canonical entity.
- Same-provider conflicts need their own review state.
- Dependent bridges inherit the risk of the bridge they depend on.
- A safe merge remains reversible.
