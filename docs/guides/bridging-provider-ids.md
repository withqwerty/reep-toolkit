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
matching_fields: [provider_id, source_snapshot, matcher_version]
confidence_floor: 0.95
---

# Bridging Provider IDs

Provider bridges are the core asset of a register. Treat them as evidence with
provenance, not as anonymous key-value pairs.

## Bridge Types

| Bridge type              | Example shape                                                      | Reep-style treatment                                        |
| ------------------------ | ------------------------------------------------------------------ | ----------------------------------------------------------- |
| Direct provider bridge   | Provider record carries another provider's ID.                     | Strong if entity type and namespace are clear.              |
| Hub bridge               | Provider A links to Wikidata or Transfermarkt, then to provider B. | Strong only if the hub link is current and typed correctly. |
| Derived community bridge | Public mapping CSV between two providers.                          | Useful, but measure and document false positives.           |
| Signal-derived bridge    | Matcher infers ID from DOB/name/team context.                      | Store with method and confidence.                           |
| Slug or URL bridge       | Provider URL segment or mutable slug.                              | Treat as weak unless scheme stability is documented.        |

## Common Bridge Routes

| Route                                        | Typical use                                                  | Caution                                                                        |
| -------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| Provider -> Transfermarkt -> target register | Football-wide player, team, coach, and competition matching. | Transfermarkt IDs are type-scoped; do not let player/team numeric IDs collide. |
| Provider -> Wikidata -> target register      | Public cross-provider bridges where Wikidata has a property. | Wikidata properties can be wrong, stale, or uneven by region/gender.           |
| TheSportsDB -> Wikidata or Transfermarkt     | Public fan API records with explicit external fields.        | Coverage is crowd-edited and partial.                                          |
| SportMonks -> Transfermarkt                  | Paid API metadata rows that carry TM IDs.                    | Verify entity type and namespace.                                              |
| FPL -> `opta_numeric`                        | Premier League players and teams.                            | `opta_numeric` is not the modern Opta UUID namespace.                          |
| Community bridge CSV -> hub provider         | FBref/TM and FPL-related mappings.                           | Measure false positives and require corroboration where possible.              |

When a pair is not directly listed, prefer routing through a typed hub over inventing a
new fuzzy path. If both sides can independently resolve to the same target-register
entity, joining on the target ID is usually safer than matching provider A directly to
provider B.

## Canonical Provider Names

Use one canonical provider namespace per provider. Do not encode entity type into the
provider name unless the upstream provider genuinely has separate namespaces that cannot
be distinguished otherwise.

Good:

```text
provider = transfermarkt
entity_type = player
external_id = 568177
```

Risky:

```text
provider = transfermarkt_player
external_id = 568177
```

Entity type belongs on the entity, the mapping row, or the lookup query. Splitting
provider names makes bridge reuse harder and hides cross-type collisions from
validators.

## Bridge Conflicts

If a new bridge conflicts with an existing bridge:

1. Compare source authority.
2. Compare confidence and method.
3. Check whether one bridge is stale, retired, or derived.
4. Preserve both pieces of evidence until the conflict is resolved.
5. Do not silently overwrite stronger curated evidence with weaker new evidence.

## Conflict Shapes

| Conflict                                                         | Meaning                                                  | Default action                                            |
| ---------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------- |
| Same provider ID attached to two live entities of the same type. | Possible duplicate or bad bridge.                        | Block auto-write; review duplicate resolution.            |
| One entity has two IDs from the same provider namespace.         | Possible upstream merge, role split, or wrong namespace. | Check provider semantics before merging.                  |
| Derived refresh disagrees with curated mapping.                  | Upstream drift or previous correction.                   | Preserve curated mapping; create review item.             |
| Player ID appears on a coach entity.                             | Could be player/coach role confusion.                    | Verify namespace and role; do not collapse automatically. |
| Team bridge crosses men's/women's/youth categories.              | Wrong team level or category.                            | Reject or split entity model.                             |

## Bridge History

Do not store only the latest accepted bridge. Keep enough history to answer:

- when the bridge first appeared,
- which source produced it,
- which matcher accepted it,
- whether it replaced weaker evidence,
- whether it has ever conflicted,
- whether it was later rejected or superseded.

This turns future refreshes into drift checks instead of archaeology.

## Bridge Lineage

Every bridge should carry:

- provider,
- external ID,
- entity type,
- method,
- confidence,
- source snapshot,
- matcher version,
- created/updated timestamps,
- review status when applicable.

Without lineage, an old mistake and a fresh high-confidence bridge look the same.

## Public Provider Pages Should Say

Every provider page should make bridge semantics explicit:

- which external IDs are exposed,
- whether they are direct or derived,
- which entity types they apply to,
- known coverage gaps,
- whether IDs are stable, legacy, slug-based, or namespaced,
- recommended confidence floor.

## Worked Example

See [Bridge conflict case study](../examples/bridge-conflict-case-study.md) for the full
routing path when a new source proposes a provider bridge that conflicts with stronger
existing evidence.
