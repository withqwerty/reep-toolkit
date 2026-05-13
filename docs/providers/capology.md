---
doc_type: provider_card
content_lane: reference
status: draft
public_safe: true
last_verified: 2026-05-13
site_section: providers
stance: descriptive
contribution_model: evidence_required
provider: capology
entity_types: [player, team, competition]
access_tier: public_grey
source_kind: living
authority_role: metadata_source
bridge_providers: []
matching_fields: [capology_slug, name, nationality, team_slug, position]
confidence_floor: 0.85
private_dependencies: []
---

# Capology

Capology is a public salary and contract reference. It can be useful downstream once a
player is identified, but its identity surface is thin because player pages do not
expose date of birth or a cross-provider bridge.

## Entity Model

| Entity type | Capology term | ID shape     | Notes                                               |
| ----------- | ------------- | ------------ | --------------------------------------------------- |
| Player      | player        | slug         | Slug can include a suffix; treat as opaque.         |
| Team        | club          | slug         | Usually a clean short club name.                    |
| Competition | league        | page/context | Not a stable provider competition bridge by itself. |
| Match       | none          | —            | Not modelled.                                       |

## Matching Surface

| Field       | Use                           | Gotcha                                |
| ----------- | ----------------------------- | ------------------------------------- |
| Player slug | Provider bridge after review. | Slug suffixes can change or redirect. |
| Player name | Candidate signal.             | No DOB means name alone is weak.      |
| Nationality | Corroboration.                | Not enough without team/context.      |
| Team slug   | Team context.                 | Team context is point-in-time.        |
| Position    | Weak corroboration.           | Inconsistent labels.                  |

## Reep-Style Linking Advice

- Treat player matches as review-first unless another source supplies DOB or a direct
  bridge.
- Use Capology team rows as useful context, not as person identity evidence.
- Keep slugs opaque; do not parse identity from the slug body or suffix.
- Record snapshot date for salary/contract fields because they are time-sensitive.

## Gotchas

- No DOB is the dominant identity constraint.
- No public Wikidata or Transfermarkt bridge is exposed.
- Slugs can carry suffixes and may redirect over time.
- Salary and contract fields are data facts, not identity evidence.

## References

- [Capology](https://www.capology.com/)
