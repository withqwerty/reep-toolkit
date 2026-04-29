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

# Loaders

Loaders convert provider-native data into stable record shapes. They should not write to
the target register and should not hide provider quirks.

## Loader Responsibilities

- Read public API responses, cached JSON, CSVs, database exports, or user-supplied
  files.
- Preserve provider IDs as strings unless numeric semantics matter.
- Normalise obvious scalar formats such as dates only when the conversion is
  deterministic.
- Keep raw fields available when a normalisation can lose meaning.
- Emit typed records that matchers can consume.

## Acquisition Policy

The public toolkit can ship different loader types by access tier:

| Access tier  | Recommended loader                                     |
| ------------ | ------------------------------------------------------ |
| Public bulk  | Fetcher plus file loader when licence allows.          |
| Public API   | Fetcher plus cached-response loader when terms permit. |
| Public grey  | Cached-response loader only.                           |
| Paid/private | User-supplied CSV/JSON loader only.                    |

## Shape Before Source

Multiple acquisition routes should emit the same shape:

```text
load_players_from_api(...) -> Iterable[ProviderPlayer]
load_players_from_json(...) -> Iterable[ProviderPlayer]
load_players_from_csv(...) -> Iterable[ProviderPlayer]
```

The matcher should not need to know which path produced the record.
