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

This roadmap describes the current post-migration work for Reep Toolkit. The first
public-safe consolidation pass is in place: this repo is now the canonical public docs,
provider-reference, worked-example, schema, and reference-script surface.

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

Before promoting the site publicly, review:

- whether the public/private boundary is strict enough,
- whether Reep is positioned as a case study rather than a hidden dependency,
- whether the front matter keys are sufficient for search and contribution workflows,
- whether the reference schema is helpful without over-prescribing Reep internals,
- whether migrated provider-card statuses match their reviewed state;
- whether any remaining `reep-scripts` material is worth preserving as public guidance
  before that repo is archived.

## Next Work

1. Finish the `reep-scripts` archive posture so it points readers here instead of
   presenting itself as an active package.
2. Promote or explicitly park any remaining provider facts from `football-docs` and
   `reep-scripts`.
3. Add custom browsing surfaces only where Markdown, the sidebar, and full-text search
   are not enough.
4. Keep the static site build, schema smoke test, reference-script smoke test, and
   public-boundary checks as the release gate.
5. Keep private breadcrumbs out of public docs as provider cards continue to improve.
