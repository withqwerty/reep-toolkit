---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: providers
stance: descriptive
contribution_model: evidence_required
---

# Provider Knowledge Base

Provider docs describe provider world models, not just API fields. Each card should
explain what the provider identifies, which IDs are stable, which fields help matching,
which bridge paths exist, and which quirks can create false positives.

## Provider Card Standard

Each provider card should include:

1. Summary.
2. Entity types identified.
3. ID namespaces and stability.
4. Matching surface by entity type.
5. Bridge data to other providers.
6. How to acquire the matching subset.
7. Source quirks and scheme changes.
8. Recommended linking strategy.
9. Known false-positive risks.
10. References and reproducible evidence.

Use [\_template.md](_template.md) for new cards.

## First Tranche

These cards are the initial public-safe provider tranche:

- [Wikidata](wikidata.md): universal cross-provider bridge and public entity spine.
- [Transfermarkt](transfermarkt.md): de facto football bridge target.
- [Opta / Stats Perform](opta.md): four distinct Opta-related ID systems.
- [SportMonks](sportmonks.md): paid API with first-class Transfermarkt bridges.
- [FBref](fbref.md): Sports Reference IDs and community bridge tables.
- [FotMob](fotmob.md): broad consumer app coverage with signal-only matching.
- [TheSportsDB](thesportsdb.md): community API with Wikipedia-to-Wikidata bridge.
- [Soccerdonna](soccerdonna.md): women's-football specialist and gender-scope signal.

The wider provider backlog is tracked in [CATALOGUE.md](CATALOGUE.md).

## Catalogue

- [Provider catalogue](CATALOGUE.md): full-card coverage and queued provider docs.
- [Source taxonomy](sources.md): how to classify providers before deciding what they can
  do in a register.

## Searchable Front Matter

Provider cards should populate:

- `provider`,
- `entity_types`,
- `access_tier`,
- `source_kind`,
- `authority_role`,
- `bridge_providers`,
- `matching_fields`,
- `confidence_floor`,
- `private_dependencies`.

## Contribution Rule

Provider facts should cite reproducible evidence:

- a public documentation page,
- an open dataset row,
- a minimal script,
- a provider payload shape the contributor is allowed to describe,
- or a public project that demonstrates the mapping.

Do not cite private local paths as the only evidence in public docs.
