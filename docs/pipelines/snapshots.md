---
doc_type: pipeline
content_lane: practice
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: pipelines
stance: opinionated
contribution_model: maintainer_doctrine
---

# Snapshots

Snapshots make matching reproducible.

## Snapshot First

Fetch or receive upstream data, write it to a durable snapshot, then run loaders and
matchers from that snapshot. Avoid matching directly against transient API responses.

## Snapshot Metadata

Recommended metadata:

- provider,
- endpoint or dataset name,
- acquisition timestamp,
- upstream version or export date,
- content hash,
- licence/access tier,
- acquisition command or script version,
- row count when applicable.

## Replay

A good pipeline can rerun:

```text
same snapshot + same matcher version + same target register state -> same candidate output
```

Register state changes can legitimately change outcomes, so store enough context to
explain both the source snapshot and the target baseline.
