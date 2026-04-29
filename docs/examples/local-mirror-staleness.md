---
doc_type: example
content_lane: example
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: examples
stance: illustrative
contribution_model: example_patch
entity_types: [player, team, match]
matching_fields: [provider_id, source_snapshot, target_store, mirror_snapshot]
confidence_floor: 0.95
failure_mode: stale_read_mirror
decision: [noop, refresh_or_report]
search_tags: [mirror, staleness, idempotency]
---

# Local Mirror Staleness

This example shows how a read mirror can make a matcher re-propose work that has already
been written to the target register.

## Situation

A pipeline uses two stores:

| Store             | Role                                                 |
| ----------------- | ---------------------------------------------------- |
| target register   | the write target and source of truth                 |
| local read mirror | fast lookup store refreshed from the target register |

At 10:00, the mirror contains:

| entity_id | provider | external_id |
| --------- | -------- | ----------- |
| `p_001`   | wikidata | Q100        |

At 10:05, a matcher writes this bridge to the target register:

```text
p_001 -> fotmob:12345
confidence: 0.95
method: dob+normalised-name
```

The local mirror has not been refreshed yet.

## Bad Follow-Up Run

At 10:10, a gap-fill matcher reads the mirror and sees no `fotmob:12345` bridge. It
re-proposes the same write:

```text
candidate:
  entity_id: p_001
  provider: fotmob
  external_id: 12345
  status: proposed_again
```

If the pipeline treats the mirror as current, it may create duplicate review items,
duplicate temp output, or confusing "new coverage" counts.

## Correct Guard

Use the target register for the final confidence and collision check:

| Check                                 | Reads from                | Reason                          |
| ------------------------------------- | ------------------------- | ------------------------------- |
| Fast candidate search                 | local mirror              | cheap broad lookup              |
| Existing accepted bridge before write | target register           | target may be newer than mirror |
| Same-provider same-type collision     | target register           | must protect the write surface  |
| Coverage and freshness report         | target + mirror timestamp | explain stale reads explicitly  |

## Outcome

The final write stage sees the target already has the bridge and downgrades the
candidate to a no-op:

```text
status: already_written
entity_id: p_001
provider: fotmob
external_id: 12345
reason: target-register bridge exists after mirror snapshot
```

## Operational Rule

If a matcher reads and writes the same logical namespace:

- record the mirror snapshot time,
- batch writes before re-running dependent matchers,
- refresh the mirror before producing final coverage numbers,
- make the write stage idempotent,
- report stale-mirror no-ops separately from genuine conflicts.

## Doctrine Demonstrated

- Fast mirrors are lookup accelerators, not source-of-truth replacements.
- Write guards must read the target register.
- Stale mirrors should create no-ops, not duplicate writes.
- Coverage reports need freshness metadata.
