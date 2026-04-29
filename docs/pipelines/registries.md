---
doc_type: pipeline
content_lane: practice
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: pipelines
stance: opinionated
contribution_model: maintainer_doctrine
entity_types: [player, team, coach, competition, season, match]
---

# Registries

A registry is the lookup interface between provider records and the target store.

## Minimal Player Registry

```python
class PlayerRegistry:
    def find_by_bridge(self, provider: str, external_id: str) -> str | None:
        ...

    def find_by_signals(
        self,
        *,
        name: str,
        date_of_birth: str | None = None,
        nationality: str | None = None,
    ) -> str | None:
        ...
```

## Minimal Team Registry

```python
class TeamRegistry:
    def find_by_bridge(self, provider: str, external_id: str) -> str | None:
        ...

    def find_by_signals(
        self,
        *,
        name: str,
        country: str | None = None,
        founded: int | None = None,
    ) -> str | None:
        ...
```

## Minimal Match Registry

```python
class MatchRegistry:
    def find_by_bridge(self, provider: str, external_id: str) -> str | None:
        ...

    def find_by_signals(
        self,
        *,
        match_date: str,
        home_team_id: str,
        away_team_id: str,
        competition_id: str | None = None,
        season_id: str | None = None,
    ) -> str | None:
        ...
```

## Strictness Belongs Here

The matcher should ask for a lookup. The registry decides whether the target store has
one unambiguous answer.

Examples:

- refuse DOB-less player lookups,
- reject multiple name+DOB candidates,
- require country for team matches,
- allow a single token-subset match only if all other candidates are absent,
- scope match lookup by season when multiple fixtures share date and teams.
