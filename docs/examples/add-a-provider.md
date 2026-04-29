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
failure_mode: provider_onboarding
decision: [document, snapshot, review]
search_tags: [provider-card, ingest, onboarding]
---

# Add a Provider

## 1. Write the Provider Card

Start with `docs/providers/_template.md`. Before coding, document:

- entity types,
- ID namespaces,
- field formats,
- bridge fields,
- access tier,
- known quirks,
- recommended confidence floors.

## 2. Decide Loader Scope

Choose the public-safe loader type:

- fetcher plus loader for public bulk data,
- cached JSON loader for grey APIs,
- user-supplied file loader for paid/private exports.

## 3. Define Records

Use provider-shaped records. Preserve provider field semantics rather than forcing every
source into one global schema too early.

## 4. Implement Matcher Cascade

Start with the strongest bridge. Add weaker fallbacks only if they produce reviewable
evidence.

## 5. Add Tests

Test:

- direct bridge match,
- strong signal match,
- ambiguous candidate rejection,
- unmatched residue,
- bad or partial source rows.

## 6. Document Write Policy

Say which outcomes can be auto-written, which require review, and which are
discovery-only.
