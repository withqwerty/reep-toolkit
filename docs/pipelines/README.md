---
doc_type: pipeline
content_lane: practice
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: pipelines
stance: opinionated
contribution_model: maintainer_doctrine
---

# Pipeline Model

The Reep-style pipeline keeps each decision point separate:

```text
acquire snapshot -> load records -> match candidates -> review weak matches -> write lineage -> export/register API
```

Each stage is replaceable. A notebook user may load CSVs into memory. A public register
may write SQLite. A vendor may resolve through a service-backed registry. The matcher
should not care.

## Pipeline Principles

- Loaders know provider shapes.
- Matchers are pure functions.
- Registries know the target store.
- Review queues preserve uncertainty.
- Writes include lineage.
- Snapshots make reruns reproducible.
