---
doc_type: taxonomy
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: contribution
stance: descriptive
contribution_model: maintainer_doctrine
---

# Front Matter Taxonomy

Every markdown page should start with YAML front matter. The goal is searchability:
agents, scripts, static-site builders, and humans should be able to filter docs by
provider, entity type, source access, matching strength, and maturity.

## Common Keys

```yaml
---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-04-29
owners: []
site_section: providers
entity_types: [player, team]
provider: transfermarkt
access_tier: public_bulk
source_kind: living
authority_role: bridge_spine
bridge_providers: [wikidata, fbref]
matching_fields: [provider_id, name, date_of_birth, nationality]
confidence_floor: 0.95
failure_mode: signal_only_provider
decision: [auto_write_if_unique, review_residue]
search_tags: [fotmob, signal-match, dob]
stance: descriptive
contribution_model: evidence_required
private_dependencies: []
---
```

## `content_lane`

- `reference`: contribution-friendly provider facts, taxonomies, and public evidence.
- `practice`: opinionated Reep-informed guidance.
- `example`: runnable or narrative examples.
- `schema`: reference schemas and machine-readable contracts.

## `stance`

- `descriptive`: explains what exists and how a provider behaves.
- `opinionated`: recommends a practice and explains why.
- `illustrative`: demonstrates one implementation without making it mandatory.

## `contribution_model`

- `evidence_required`: contributors can update the page with reproducible evidence.
- `maintainer_doctrine`: changes should be reviewed as doctrine or operating practice.
- `example_patch`: contributions should keep the example small and reproducible.

## `doc_type`

- `project_overview`
- `docs_index`
- `taxonomy`
- `provider_card`
- `provider_template`
- `world_model`
- `practice_guide`
- `pipeline`
- `example`
- `examples_catalogue`
- `schema`

## `status`

- `draft`: useful first pass, needs review.
- `reviewed`: maintainer-reviewed and public-safe.
- `stable`: treated as public reference.
- `deprecated`: superseded but retained for history.

## `access_tier`

- `public_bulk`: explicitly published data dumps or repos.
- `public_api`: documented public API suitable for programmatic use.
- `public_grey`: reachable public surface with unclear re-use terms.
- `paid_or_private`: customer-gated, licensed, or auth-walled.
- `derived_public`: public bridge dataset derived from another provider.
- `unknown`: needs research before recommending ingestion.

## `source_kind`

- `living`: records evolve over time and need refresh tracking.
- `static`: a fixed historical dataset.
- `mixed`: some stable IDs, some evolving metadata.

## `authority_role`

- `canonical_candidate`: plausible source for creating entities in a register.
- `bridge_spine`: strong cross-provider bridge source.
- `metadata_source`: useful for aliases, DOB, nationality, position, or disambiguation.
- `coverage_probe`: useful for detecting gaps rather than creating entities.
- `consumer_only`: useful downstream but weak for identity matching.

## `confidence_floor`

Use this as a routing label, not a probability claim:

- `1.0`: direct stable bridge from a trusted source.
- `0.95`: strong biographical match, normally safe to write if ambiguity is rejected.
- `0.90`: useful corroboration or derived bridge, route to review unless independently
  confirmed.
- `<0.90`: weak signal, never auto-write in a public register.

## Example Search Keys

Worked examples must also carry:

- `failure_mode`: the specific class of problem, such as `provider_namespace_mismatch`,
  `duplicate_player`, or `stale_read_mirror`.
- `decision`: the routing outcome, such as `auto_write_if_unique`, `review`, `reject`,
  `tombstone`, `candidate_only`, or `rewrite_namespace`.
- `search_tags`: short tags for faceted search and catalogue generation.

Regenerate [examples/CATALOGUE.md](examples/CATALOGUE.md) after changing example front
matter:

```bash
npm run docs:catalogue
```
