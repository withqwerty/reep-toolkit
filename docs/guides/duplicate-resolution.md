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
matching_fields: [provider_id, alias, source_snapshot]
confidence_floor: 0.95
---

# Duplicate Resolution

Duplicates are inevitable in a growing football register. The goal is not to pretend
they will never happen. The goal is to make resolution safe, auditable, and
non-breaking.

## Reep-Style Rule

Keep one canonical entity. Retire the duplicate with a redirect. Move or reconcile
non-conflicting data onto the canonical entity. Preserve conflicting evidence for audit
and review.

Do not hard-delete a published entity ID just because it is now known to be a duplicate.

## Merge Shape

When entity `B` is a duplicate of entity `A`:

```text
A remains canonical
B is tombstoned
B.canonical_entity_id = A
non-conflicting bridges move from B to A
aliases from B move to A
conflicting bridges remain flagged for review
downstream consumers can resolve B -> A
```

## What Moves

Move when it does not create a conflict:

- provider IDs,
- aliases,
- language variants,
- source metadata,
- non-contradictory biographical fields,
- review history.

## Data Movement Rules

| Data type                                                 | Move to canonical?                               | Notes                                             |
| --------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------- |
| Provider bridge, no same-provider conflict                | Yes                                              | Preserve original source and timestamps.          |
| Provider bridge, conflicts with canonical provider bridge | No automatic move                                | Create a conflict review item.                    |
| Alias                                                     | Yes                                              | Keep provider/language/source.                    |
| Rejected candidate                                        | Yes, or relink to canonical                      | It prevents repeated bad proposals.               |
| Date of birth                                             | Only if canonical is empty or values agree       | Contradiction needs review.                       |
| Country/nationality                                       | Merge as multi-value evidence where model allows | Do not overwrite stronger sourced fields blindly. |
| Match participation                                       | Usually no                                       | Match duplicates need fixture-level review.       |
| Search index text                                         | Rebuild                                          | Derived data should be rebuilt, not hand-moved.   |

## What Needs Review

Do not blindly merge:

- two different external IDs from the same provider and entity type,
- contradictory dates of birth,
- contradictory team identity fields,
- match records with different dates or participants,
- provider bridges with known upstream retirement or reassignment.

## Tombstone Versus Delete

Use tombstones for published IDs:

| Action                  | When to use                                                                                      |
| ----------------------- | ------------------------------------------------------------------------------------------------ |
| Tombstone with redirect | Published entity was duplicate or superseded.                                                    |
| Hard delete             | Unpublished staging-only mistake, scratch fixture, or same-session bad mint before external use. |
| Split                   | Two real entities were incorrectly merged.                                                       |

## Merge Audit Fields

Store:

- retired entity ID,
- canonical entity ID,
- merge reason,
- evidence summary,
- operator or reviewer,
- timestamp,
- moved bridge count,
- conflicts left behind.

## Split After Bad Merge

Sometimes the register discovers that an earlier merge was wrong. To make splits
possible:

- keep the merge audit packet,
- keep bridge history,
- keep rejected and accepted decisions,
- avoid destructive deletes of the retired entity,
- make moved rows traceable to their original entity.

If a merge cannot be undone, it was not a safe merge.

## Consumer Behaviour

APIs and exports should allow consumers to discover redirects. A lookup for the retired
ID should not silently disappear.

## Worked Examples

- [Duplicate player merge](../examples/duplicate-player-merge.md): non-conflicting
  duplicate merge.
- [Duplicate merge with provider conflict](../examples/duplicate-merge-with-provider-conflict.md):
  duplicate merge where same-provider ID conflicts block automatic data movement.
