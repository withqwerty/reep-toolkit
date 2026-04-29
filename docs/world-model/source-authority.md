---
doc_type: world_model
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: world-model
stance: descriptive
contribution_model: maintainer_doctrine
entity_types: [player, team, coach, competition, season, match]
---

# Source Authority

No provider is authoritative for every entity type. A register should document which
source is allowed to create or confirm each type of entity.

## Authority Roles

| Role                 | Meaning                                                                |
| -------------------- | ---------------------------------------------------------------------- |
| Canonical candidate  | Good enough to create new register entities under a documented policy. |
| Bridge spine         | Strong cross-provider ID source, even if not used for creation.        |
| Metadata source      | Useful for DOB, aliases, nationality, positions, or disambiguation.    |
| Coverage probe       | Useful for finding gaps or candidates.                                 |
| Consumer-only source | Useful downstream, weak for identity creation.                         |

## Choosing Sources

For each entity type, document:

- which providers can create new entities,
- which providers can attach bridges only,
- which providers can add aliases or metadata only,
- which providers require review,
- what evidence can override stale data.

## Public Versus Private Authority

The public toolkit should teach the pattern, not leak a private register's exact
operational policy. A good public statement:

> Choose a canonical source per entity type and make non-canonical providers attach as
> bridges unless independent evidence confirms a new entity.

A poor public statement:

> Run this private script against this local paid snapshot and promote the result to
> production.

## Source Drift

Provider data drifts:

- IDs merge or retire,
- slugs change,
- names are restyled,
- teams rebrand,
- seasons are restructured,
- match dates move,
- bridge datasets are corrected.

Snapshot, version, and validate every update.
