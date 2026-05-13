---
doc_type: migration_manifest
content_lane: reference
status: draft
public_safe: false
publish: false
last_verified: 2026-05-13
site_section: internal
stance: descriptive
contribution_model: maintainer_doctrine
---

# Reep Scripts Migration Manifest

This manifest tracks the useful public material in `reep-scripts` so it can be folded
into `reep-toolkit` and the old package/docs surface can be frozen or archived.

The inventory was taken from the local `reep-scripts` checkout on 2026-05-13. Paths
below are repo-relative to `reep-scripts`; destinations are repo-relative to
`reep-toolkit`.

## Disposition Keys

| Disposition   | Meaning                                                                      |
| ------------- | ---------------------------------------------------------------------------- |
| `migrate`     | Bring across with light editing and toolkit front matter.                    |
| `rewrite`     | Preserve the concept, but rewrite for toolkit terminology and public safety. |
| `drop`        | Do not bring across.                                                         |
| `archive`     | Keep historical only; do not present as active toolkit material.             |
| `source_only` | Use as evidence or comparison material, not as copied content.               |

## Summary

| Source class               | Count | Phase   | Default disposition                 |
| -------------------------- | ----: | ------- | ----------------------------------- |
| Markdown docs              |    41 | Phase 2 | `migrate` or `rewrite`              |
| Provider docs              |    33 | Phase 2 | `migrate` or `rewrite`              |
| Evidence/template fixtures |     7 | Phase 3 | `migrate`                           |
| Schema files               |     2 | Phase 3 | `rewrite`                           |
| Python modules             |    41 | Phase 3 | `rewrite`, `source_only`, or `drop` |
| Tests                      |    30 | Phase 3 | `source_only`                       |
| Package/build metadata     |     8 | Phase 5 | `drop` or `archive`                 |

## Markdown Docs

| Source path                        | Destination                                                 | Disposition   | Public-safe review | Evidence status | Verification           |
| ---------------------------------- | ----------------------------------------------------------- | ------------- | ------------------ | --------------- | ---------------------- |
| `README.md`                        | `README.md`                                                 | `rewrite`     | pass               | checked         | docs review            |
| `CONTRIBUTING.md`                  | `CONTRIBUTING.md`                                           | `rewrite`     | pending            | not_applicable  | docs review            |
| `CHANGELOG.md`                     | none                                                        | `archive`     | pending            | not_applicable  | none                   |
| `docs/architecture.md`             | `docs/pipelines/architecture.md`                            | `rewrite`     | pass               | checked         | docs review            |
| `docs/cross-provider-matching.md`  | `docs/guides/relationship-constrained-provider-matching.md` | `rewrite`     | pass               | checked         | docs review            |
| `docs/identity/evidence-schema.md` | `docs/templates/evidence-schema.md`                         | `rewrite`     | pass               | synthetic_only  | schema validation      |
| `docs/matching-field-alignment.md` | `docs/guides/matching-thresholds.md`                        | `rewrite`     | pass               | checked         | docs review            |
| `docs/matching.md`                 | `docs/guides/bridging-provider-ids.md`                      | `rewrite`     | pass               | checked         | docs review            |
| `docs/reep-next.md`                | none                                                        | `source_only` | pending            | not_applicable  | public-boundary review |
| `docs/schema.md`                   | `docs/schemas/README.md`                                    | `rewrite`     | pass               | synthetic_only  | schema validation      |
| `docs/templates/README.md`         | `docs/templates/README.md`                                  | `rewrite`     | pass               | checked         | fixture smoke test     |

## Provider Docs

| Source path                              | Destination                             | Disposition | Public-safe review | Evidence status | Verification         |
| ---------------------------------------- | --------------------------------------- | ----------- | ------------------ | --------------- | -------------------- |
| `docs/providers/README.md`               | `docs/providers/README.md`              | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/CATALOGUE.md`            | `docs/providers/CATALOGUE.md`           | `migrate`   | pass               | checked         | catalogue generation |
| `docs/providers/sources.md`              | `docs/providers/sources.md`             | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/ecosystem-notes.md`      | `docs/providers/ecosystem-notes.md`     | `rewrite`   | pending            | needs_source    | docs review          |
| `docs/providers/api-football.md`         | `docs/providers/api-football.md`        | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/capology.md`             | `docs/providers/capology.md`            | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/clubelo.md`              | `docs/providers/clubelo.md`             | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/datafactory.md`          | `docs/providers/datafactory.md`         | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/fbref.md`                | `docs/providers/fbref.md`               | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/football-data-co-uk.md`  | `docs/providers/football-data-co-uk.md` | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/fotmob.md`               | `docs/providers/fotmob.md`              | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/fpl.md`                  | `docs/providers/fpl.md`                 | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/hawkeye.md`              | `docs/providers/hawkeye.md`             | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/impect-ecosystem.md`     | `docs/providers/impect.md`              | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/livesport.md`            | `docs/providers/livesport.md`           | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/metrica.md`              | `docs/providers/metrica.md`             | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/opta.md`                 | `docs/providers/opta.md`                | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/pff.md`                  | `docs/providers/pff.md`                 | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/secondspectrum.md`       | `docs/providers/secondspectrum.md`      | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/signality.md`            | `docs/providers/signality.md`           | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/skillcorner-tracking.md` | `docs/providers/skillcorner.md`         | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/soccerdonna.md`          | `docs/providers/soccerdonna.md`         | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/sofifa.md`               | `docs/providers/sofifa.md`              | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/sportec.md`              | `docs/providers/sportec.md`             | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/sportmonks.md`           | `docs/providers/sportmonks.md`          | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/sportradar.md`           | `docs/providers/sportradar.md`          | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/statsbomb.md`            | `docs/providers/statsbomb.md`           | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/thesportsdb.md`          | `docs/providers/thesportsdb.md`         | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/tracab.md`               | `docs/providers/tracab.md`              | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/transfermarkt.md`        | `docs/providers/transfermarkt.md`       | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/understat.md`            | `docs/providers/understat.md`           | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/whoscored.md`            | `docs/providers/whoscored.md`           | `rewrite`   | pass               | checked         | docs review          |
| `docs/providers/wikidata.md`             | `docs/providers/wikidata.md`            | `rewrite`   | pass               | checked         | docs review          |

## Fixtures And Schemas

| Source path                                                  | Destination                                                  | Disposition   | Public-safe review | Evidence status | Verification       |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------- | ------------------ | --------------- | ------------------ |
| `fixtures/evidence/example-match-candidate.json`             | `fixtures/evidence/example-match-candidate.json`             | `migrate`     | pass               | synthetic_only  | fixture smoke test |
| `fixtures/evidence/review-residue.json`                      | `fixtures/evidence/review-residue.json`                      | `migrate`     | pass               | synthetic_only  | fixture smoke test |
| `fixtures/evidence/source-constraints.json`                  | `fixtures/evidence/source-constraints.json`                  | `migrate`     | pass               | synthetic_only  | fixture smoke test |
| `fixtures/templates/candidate-recovery-residue.json`         | `fixtures/templates/candidate-recovery-residue.json`         | `migrate`     | pass               | synthetic_only  | fixture smoke test |
| `fixtures/templates/match-bridge-candidate.json`             | `fixtures/templates/match-bridge-candidate.json`             | `migrate`     | pass               | synthetic_only  | fixture smoke test |
| `fixtures/templates/relationship-constrained-candidate.json` | `fixtures/templates/relationship-constrained-candidate.json` | `migrate`     | pass               | synthetic_only  | fixture smoke test |
| `fixtures/templates/split-season-stage-candidates.json`      | `fixtures/templates/split-season-stage-candidates.json`      | `migrate`     | pass               | synthetic_only  | fixture smoke test |
| `schemas/reference-schema.sql`                               | `schemas/reference-register.sql`                             | `rewrite`     | pass               | synthetic_only  | schema validation  |
| `schemas/migrations/0001_add_lineage_columns.sql`            | none                                                         | `source_only` | pending            | synthetic_only  | schema review      |

## Python Source Families

| Source family                   | Destination                                          | Disposition   | Public-safe review | Evidence status | Verification           |
| ------------------------------- | ---------------------------------------------------- | ------------- | ------------------ | --------------- | ---------------------- |
| `reep_scripts/evidence.py`      | `schemas/` and `reference-scripts/evidence/`         | `rewrite`     | pending            | synthetic_only  | schema validation      |
| `reep_scripts/templates/`       | `docs/templates/` and `reference-scripts/templates/` | `rewrite`     | pending            | synthetic_only  | fixture smoke test     |
| `reep_scripts/standardise/`     | `reference-scripts/normalisation/`                   | `rewrite`     | pending            | synthetic_only  | fixture smoke test     |
| `reep_scripts/loaders/`         | `reference-scripts/loaders/`                         | `rewrite`     | pending            | synthetic_only  | fixture smoke test     |
| `reep_scripts/matchers/`        | `reference-scripts/matchers/`                        | `rewrite`     | pending            | synthetic_only  | fixture smoke test     |
| `reep_scripts/linkage/`         | `reference-scripts/writes/`                          | `rewrite`     | pending            | synthetic_only  | fixture smoke test     |
| `reep_scripts/adapters/`        | none                                                 | `source_only` | pending            | not_applicable  | docs review            |
| `reep_scripts/matchers/reep.py` | none                                                 | `source_only` | pending            | not_applicable  | public-boundary review |
| `reep_scripts/config.py`        | none                                                 | `drop`        | pending            | not_applicable  | none                   |
| `reep_scripts/__init__.py`      | none                                                 | `drop`        | pending            | not_applicable  | none                   |

## Tests

| Source family                 | Destination                                 | Disposition   | Public-safe review | Evidence status | Verification       |
| ----------------------------- | ------------------------------------------- | ------------- | ------------------ | --------------- | ------------------ |
| `tests/test_evidence.py`      | `tests/reference/test_evidence_examples.py` | `rewrite`     | pending            | synthetic_only  | fixture smoke test |
| `tests/test_templates.py`     | `tests/reference/test_template_examples.py` | `rewrite`     | pending            | synthetic_only  | fixture smoke test |
| `tests/test_*_loader.py`      | `tests/reference/test_loader_examples.py`   | `source_only` | pending            | synthetic_only  | fixture smoke test |
| `tests/test_*_matcher.py`     | `tests/reference/test_matcher_examples.py`  | `source_only` | pending            | synthetic_only  | fixture smoke test |
| `tests/test_*fixtures*.py`    | `tests/reference/`                          | `source_only` | pending            | synthetic_only  | fixture smoke test |
| `tests/test_adapters.py`      | none                                        | `drop`        | pending            | not_applicable  | none               |
| `tests/test_reep_registry.py` | none                                        | `drop`        | pending            | not_applicable  | none               |
| `tests/test_library_api.py`   | none                                        | `drop`        | pending            | not_applicable  | none               |

## Package And Build Metadata

| Source path                           | Destination | Disposition   | Public-safe review | Evidence status | Verification |
| ------------------------------------- | ----------- | ------------- | ------------------ | --------------- | ------------ |
| `pyproject.toml`                      | none        | `drop`        | pending            | not_applicable  | none         |
| `.github/workflows/test.yml`          | none        | `source_only` | pending            | not_applicable  | CI review    |
| `.gitignore`                          | none        | `source_only` | pending            | not_applicable  | none         |
| `LICENSE`                             | `LICENSE`   | `migrate`     | pending            | not_applicable  | docs review  |
| `reep_scripts.egg-info/PKG-INFO`      | none        | `archive`     | pending            | not_applicable  | none         |
| `reep_scripts.egg-info/SOURCES.txt`   | none        | `archive`     | pending            | not_applicable  | none         |
| `reep_scripts.egg-info/requires.txt`  | none        | `archive`     | pending            | not_applicable  | none         |
| `reep_scripts.egg-info/top_level.txt` | none        | `archive`     | pending            | not_applicable  | none         |

## Phase 2 Provider Priority

1. Reconcile providers already present in both repos: Transfermarkt, Opta, SportMonks,
   Soccerdonna, Wikidata, FBref, FotMob, and TheSportsDB.
2. Promote high-value provider cards currently only in `reep-scripts`: StatsBomb,
   Wyscout/WhoScored-adjacent material, SkillCorner, Impect, Sportradar, SoFIFA,
   Capology, API-Football, and football-data.co.uk.
3. Queue lower-priority or non-identity-heavy cards as draft provider notes.

Do not mark a manifest row as resolved until the destination page or example has passed
the docs checks and any required fixture/schema smoke test.
