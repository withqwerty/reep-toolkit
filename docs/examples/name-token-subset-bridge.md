---
doc_type: example
content_lane: example
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: examples
stance: illustrative
contribution_model: example_patch
entity_types: [coach, player]
matching_fields: [name, date_of_birth, provider_id, token_subset, source_snapshot]
confidence_floor: 0.95
failure_mode: long_name_variant
decision: [auto_write_if_unique, review_if_ambiguous]
search_tags: [name-token, dob, alias]
---

# Name-Token Subset Bridge

This example shows a controlled fallback for names that differ by surname length,
particles, or provider display style.

## Situation

A register has a deferred coach candidate from one source:

| deferred_id | name                | date_of_birth | source_provider |
| ----------- | ------------------- | ------------- | --------------- |
| `d_001`     | Miguel Garcia Lopez | 1974-02-10    | provider_a      |

A local provider mirror has:

| mirror_id | name          | date_of_birth | provider      | external_id |
| --------- | ------------- | ------------- | ------------- | ----------- |
| `m_001`   | Miguel Garcia | 1974-02-10    | transfermarkt | 7001        |
| `m_002`   | Miguel Santos | 1974-02-10    | transfermarkt | 7002        |

Exact-name matching misses `Miguel Garcia` because the deferred record has a second
surname.

## Token Gate

Normalise names by:

- lowercasing,
- removing diacritics,
- dropping low-signal particles such as `de`, `del`, `la`, `van`, `von`,
- keeping meaningful name tokens.

Then require the provider mirror tokens to be a subset of the deferred-name tokens, with
at least two surviving mirror tokens.

| Mirror name   | Mirror tokens      | Deferred tokens             | Result |
| ------------- | ------------------ | --------------------------- | ------ |
| Miguel Garcia | `miguel`, `garcia` | `miguel`, `garcia`, `lopez` | pass   |
| Miguel Santos | `miguel`, `santos` | `miguel`, `garcia`, `lopez` | fail   |

## DOB Gate

The name-token gate is not enough. Require date-of-birth corroboration:

```text
abs(source_dob - mirror_dob) <= 1 day
```

The ±1 day tolerance handles timezone or source-entry errors. It does not excuse missing
DOB evidence.

## Uniqueness Gate

After DOB and token filtering, exactly one candidate remains:

```text
d_001 -> transfermarkt:7001
method: dob+token-subset
confidence: 0.95
```

If two candidates survive, defer to review.

## Write Set

```text
entity_id: c_001
provider: transfermarkt
external_id: 7001
confidence: 0.95
method: dob+token-subset
source_snapshot: provider-a-deferred-2026-04-29
mirror_snapshot: transfermarkt-coaches-2026-04-29
```

Add the shorter provider name as an alias:

```text
entity_id: c_001
alias: Miguel Garcia
source_provider: transfermarkt
```

## What Not To Do

Do not:

- accept one-token matches,
- use name-token subset without DOB,
- choose the first candidate when multiple rows survive,
- treat nationality as a replacement for DOB,
- overwrite an existing same-provider bridge.

## Doctrine Demonstrated

- Exact names are often too strict for football identity work.
- Token-subset matching can be safe when gated by DOB and uniqueness.
- Ambiguity still wins over convenience.
- Aliases should be harvested as evidence, not used to hide uncertainty.
