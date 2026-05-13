---
doc_type: migration_boundary
content_lane: reference
status: draft
public_safe: false
publish: false
last_verified: 2026-05-13
site_section: internal
stance: descriptive
contribution_model: maintainer_doctrine
---

# Football Docs Boundary

`football-docs` is useful source material for `reep-toolkit`, but it should not become a
second public authority for provider identity guidance.

## Launch Role

At launch, `reep-toolkit` is the public provider-reference surface. `football-docs`
remains a research/backend source that can inform toolkit pages, especially where it
documents provider data models, identity surfaces, event models, or access constraints.

The public site should not link readers to `football-docs` as a required companion
surface. If a claim is important to toolkit readers, migrate or cite it in the toolkit.

## Migration Classes

| Source class                            | Toolkit treatment              | Notes                                                                                    |
| --------------------------------------- | ------------------------------ | ---------------------------------------------------------------------------------------- |
| Identity surfaces                       | Migrate or cite                | Highest priority for provider cards.                                                     |
| Provider data models                    | Migrate selectively            | Keep fields that affect identity, provenance, or matching.                               |
| API access notes                        | Rewrite                        | Describe accepted input shapes and official source references, not acquisition workflow. |
| Event models and qualifiers             | Defer unless identity-relevant | Useful later, but not launch-critical for entity resolution.                             |
| Coordinate systems and analytics models | Defer                          | Out of scope for the first identity-resolution site.                                     |
| Open-source package usage docs          | Defer or cite externally       | Keep only where it teaches source-shape interpretation.                                  |

## Provider Priority

| Provider or surface                         | Current treatment                                                        |
| ------------------------------------------- | ------------------------------------------------------------------------ |
| Transfermarkt identity surfaces             | Compare against toolkit provider card before Phase 2 closeout.           |
| Opta identity surfaces and API access       | Migrate identity-shape claims; keep operational fetch detail out.        |
| StatsBomb identity and data model docs      | Migrate identity-shape claims where public and provider-grounded.        |
| SportMonks identity and data model docs     | Compare against existing toolkit card and reconcile bridge language.     |
| Soccerdonna identity surfaces               | Compare against existing toolkit card, especially gender-scope language. |
| SkillCorner, Wyscout, Impect                | Queue as provider cards or future provider notes.                        |
| kloppy, mplsoccer, socceraction, databallpy | Defer as tooling/docs references, not provider identity authority.       |

## Acceptance Rule

Phase 2 provider consolidation is not done until each relevant `football-docs` provider
claim is in one of three states:

1. migrated into a toolkit provider or guide page;
2. cited as supporting evidence in a toolkit page;
3. explicitly deferred as non-launch or non-identity material.

Do not copy content blindly. Reconcile it against toolkit source-role language,
public/private boundary rules, and current Reep Next terminology before migration.
