---
doc_type: practice_guide
content_lane: practice
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: guides
stance: opinionated
contribution_model: maintainer_doctrine
---

# Practice Guides

These guides are the opinionated layer of Reep Toolkit. They are not neutral
descriptions of every possible way to build a register. They explain the practices Reep
uses or has learned from: what to auto-write, what to review, when to mint, when to
defer, how to treat provider bridges, and how to merge duplicate entities without
breaking downstream users.

The guides must be public-safe. They do not cite private file paths, local snapshots,
credentials, deployment procedures, or one-off production commands.

## Guide Principles

- Explain the decision, not the private implementation.
- Prefer precise doctrine over vague advice.
- Name the failure mode the rule prevents.
- Show enough examples for a maintainer to apply the rule.
- Keep provider-specific facts in provider reference pages and link to them from guides.

## Current Guides

- [Before you ingest](before-you-ingest.md)
- [Golden path provider ingest](golden-path-provider-ingest.md)
- [Matching thresholds](matching-thresholds.md)
- [Bridging provider IDs](bridging-provider-ids.md)
- [Relationship-constrained provider matching](relationship-constrained-provider-matching.md)
- [Minting and entity creation](minting-and-entity-creation.md)
- [Duplicate resolution](duplicate-resolution.md)
- [Register maintenance](register-maintenance.md)
