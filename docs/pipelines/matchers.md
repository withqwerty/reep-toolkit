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

# Matchers

Matchers are pure functions that turn provider records into candidate links.

## Contract

```python
outcome = match_provider(records, registry)
```

The outcome should contain:

- matched records,
- unmatched records,
- rejected or ambiguous records when useful,
- method labels,
- confidence labels,
- enough evidence for review.

## Cascade Pattern

A typical player cascade:

1. Direct provider bridge.
2. Trusted cross-provider bridge.
3. DOB plus normalised name.
4. DOB plus alias.
5. Name plus nationality as review candidate.
6. Unmatched.

A typical team cascade:

1. Direct provider bridge.
2. Trusted cross-provider bridge.
3. Name plus country.
4. Name plus competition context.
5. Name-only as review candidate.
6. Unmatched.

A typical match cascade:

1. Direct provider match ID bridge.
2. Provider fixture ID through known mapping.
3. Date plus resolved home and away teams.
4. Date plus teams plus competition/season.
5. Review or unmatched.

## No Writes

Matchers should not write to the register. This keeps them reusable, testable, and safe
to run as dry-run audits.
