---
doc_type: project_overview
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: contribution
stance: opinionated
contribution_model: maintainer_doctrine
---

# Editorial Standard

These docs should read like a guide written by maintainers who have built a football
register, not like neutral generated documentation.

## What Good Looks Like

Good pages:

- tell the reader what to check before ingesting data,
- explain the failure mode behind each rule,
- separate provider facts from Reep-style recommendations,
- preserve public/private boundaries,
- make review and confidence routing explicit,
- say when to defer rather than forcing a write,
- cite public evidence for provider claims.

## Avoid

- private file paths,
- private scripts or command names,
- paid snapshot details,
- vague claims such as "this is useful",
- generic "you can implement this however you want" prose,
- repeating the same caveat without naming the consequence,
- provider facts with no evidence trail.

## Rewrite Pattern

Weak:

> This provider has some useful data and can be used for matching.

Sharp:

> This provider has no direct bridges. Use DOB plus normalised name for player
> candidates, route DOB-less records to review, and do not mint from name-only evidence.

Weak:

> Duplicates should be handled carefully.

Sharp:

> Keep one canonical entity, tombstone the duplicate, redirect the retired ID, move
> non-conflicting bridges and aliases, and preserve conflicting provider IDs for review.

Weak:

> This is how Reep does it internally.

Sharp:

> Reep's public recommendation is to keep creation sources narrow: most providers attach
> bridges or aliases first and only mint after the source-authority policy allows it.
