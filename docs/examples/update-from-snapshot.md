---
doc_type: example
content_lane: example
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: examples
stance: illustrative
contribution_model: example_patch
entity_types: [player, team, coach, competition, season, match]
failure_mode: snapshot_refresh
decision: [diff, review, write_delta]
search_tags: [snapshot, update, drift]
---

# Update From a Snapshot

## 1. Capture or Receive Snapshot

Record provider, endpoint, export date, content hash, and acquisition notes.

## 2. Load Records

Run the loader and count records by entity type. Fail early on schema drift.

## 3. Dry-Run Match

Produce a candidate output with:

- matched records,
- weak candidates,
- ambiguous candidates,
- unmatched records,
- method and confidence labels.

## 4. Compare With Previous Run

Look for:

- disappeared mappings,
- changed provider IDs,
- confidence downgrades,
- sudden row-count shifts,
- new duplicate external IDs.

## 5. Review Weak Matches

Only promote weak matches after review or independent corroboration.

## 6. Write With Lineage

Write mappings with `source_snapshot` and `matcher_version`. Keep rejected candidates so
they do not reappear as unresolved work.
