---
doc_type: practice_guide
content_lane: practice
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: guides
stance: opinionated
contribution_model: maintainer_doctrine
entity_types: [player, team, coach, competition, season, match]
---

# Register Maintenance

A register is not a one-off matching project. It is a maintained data product.

## Recurring Checks

Run checks for:

- duplicate provider IDs within the same entity type,
- one provider ID attached to multiple live entities,
- disappeared mappings from a refreshed source,
- confidence downgrades,
- stale snapshots,
- provider scheme changes,
- tombstone chains,
- unresolved weak-match queues,
- sudden coverage changes by provider or competition.

## Freshness Is Not Always Better

New upstream data can be worse than old curated data. A refresh should not blindly
overwrite:

- reviewed bridges,
- manual corrections,
- redirects,
- rejected candidates,
- known source-specific exceptions.

## Drift Reports

A useful drift report should answer:

- What changed since the last snapshot?
- Which changes are safe automatic updates?
- Which changes conflict with stronger evidence?
- Which changes indicate provider schema drift?
- Which changes affect public IDs or exported bridges?

## Maintenance Cadence

| Cadence                  | Checks                                                                                                           |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| Every ingest             | Schema drift, row counts, duplicate provider IDs, conflicting bridges, unmatched/residue counts.                 |
| Weekly or release-bound  | Source freshness, confidence downgrades, new bridge conflicts, tombstone redirects, review queue age.            |
| Monthly or tranche-bound | Provider coverage by entity type, missing high-value bridges, stale provider cards, source-authority changes.    |
| Before public export     | No disappearing public IDs, no unresolved high-severity conflicts, redirect chains collapse to one canonical ID. |

## Maintenance Doctrine

Prefer:

- snapshot-first ingestion,
- dry-run candidate output,
- confidence-aware writes,
- review queues for weak evidence,
- tombstones and redirects for retired IDs,
- explicit provider source-authority policy.

Avoid:

- live API matching without snapshots,
- name-only auto-writes,
- deleting public IDs,
- overwriting curated mappings with derived refreshes,
- hiding rejected candidates.

## What "Healthy" Looks Like

A healthy register has:

- explainable public IDs,
- stable redirects for retired IDs,
- low duplicate-provider-ID counts within entity type,
- a review queue that shrinks or is consciously accepted,
- provider cards that match current source behaviour,
- reproducible snapshots for every meaningful write batch,
- drift reports that are read before promotion.

The aim is not zero uncertainty. The aim is visible uncertainty that does not silently
corrupt public mappings.
