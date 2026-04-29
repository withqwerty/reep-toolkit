---
doc_type: project_overview
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: home
stance: descriptive
contribution_model: maintainer_doctrine
---

# Roadmap

This roadmap describes the draft scope for the first public-safe Reep Toolkit pass.

## V1 Draft

Status: complete as a first pass.

Scope:

- standalone folder and documentation structure,
- searchable front matter taxonomy,
- content lanes for provider reference, opinionated practice guides, examples, and
  schemas,
- world-model handbook,
- Reep-style practice guides for thresholds, bridging, minting, duplicates, and
  maintenance,
- first provider-card tranche and provider coverage catalogue,
- provider documentation template and source taxonomy,
- pipeline guides,
- narrative examples plus concrete worked examples for bridges, signal-only matches,
  namespace validation, team collisions, fixture identity, duplicate merges, bridge
  conflicts, provider ingest walkthroughs, and snapshot drift,
- optional reference schema,
- explicit public/private boundary.

## Review Gate

Before promoting this to a public repository or folding it into `reep-scripts`, review:

- whether the public/private boundary is strict enough,
- whether Reep is positioned as a case study rather than a hidden dependency,
- whether the front matter keys are sufficient for search and contribution workflows,
- whether the reference schema is helpful without over-prescribing Reep internals,
- which provider cards should be migrated first.

## Next Work

1. Reconcile this draft against `../reep-scripts`.
2. Promote queued provider cards from the catalogue in priority order.
3. Turn the worked examples into runnable examples once the document shape is accepted.
4. Add a generated search index or static-site build if this becomes a public site.
5. Keep private breadcrumbs out of public docs as provider cards are migrated.
