---
doc_type: example
content_lane: example
status: draft
public_safe: true
last_verified: 2026-04-29
site_section: examples
stance: illustrative
contribution_model: example_patch
---

# Examples

These examples turn the guide doctrine into concrete decisions. They use small
public-safe records, invented register IDs, and explicit outcomes so readers can see
what would be written, reviewed, deferred, or rejected.

## Where Examples Come From

The best examples come from reusable classes of real incidents:

- provider cards that reveal an unexpected world model,
- bridge conflicts where a new source disagrees with curated evidence,
- duplicate reviews caused by aliases or abbreviated names,
- type or namespace collisions in provider IDs,
- snapshot refreshes that change structure or meaning,
- review queues where weak candidates should be retained but not written.

When adapting a real incident, keep the lesson and remove private execution detail.
Examples should use invented IDs, small records, and public-safe provider descriptions.

## Build and Ingest

- [Build a small register](build-a-small-register.md).
- [Add a provider](add-a-provider.md).
- [Update from a snapshot](update-from-snapshot.md).
- [Review weak matches](review-weak-matches.md).

## Worked Matching Examples

- [Examples catalogue](CATALOGUE.md): generated table of failure modes, decisions, and
  search tags.
- [SportMonks Transfermarkt bridge](sportmonks-transfermarkt-bridge.md): direct bridge,
  auto-write, and fallback residue.
- [FotMob signal-only player match](fotmob-signal-only-player.md): DOB/name matching
  without provider bridges.
- [Women-only prior beats fuzzy bridge](women-only-prior-fuzzy-bridge.md): source
  authority beats a fuzzy id-finder confidence score.
- [Opta namespace confusion](opta-namespace-confusion.md): reject a bad Opta ID write
  before it corrupts the register.
- [Type-gated provider ID lookup](type-gated-provider-id-lookup.md): why lookups need
  entity type, not just provider plus external ID.
- [Alias variant duplicate prevention](alias-variant-duplicate-prevention.md): avoid
  minting a second player when sources use different name variants.
- [Name-token subset bridge](name-token-subset-bridge.md): controlled DOB-gated fallback
  for long-name variants.
- [Team name collision](team-name-collision.md): why name-only team matching routes to
  review.
- [Semantic team prefix collision](semantic-team-prefix-collision.md): distinguish
  semantic club-name prefixes from removable corporate forms.
- [Fixture-overlap team bridge](fixture-overlap-team-bridge.md): use fixture behaviour
  as corroboration when direct team IDs are missing.
- [Match fixture identity](match-fixture-identity.md): resolving a fixture by date and
  teams without treating event payloads as identity.
- [SportMonks stage and season mismatch](sportmonks-stage-season-mismatch.md): map
  provider season and stage IDs to the right register level.
- [Structural season ID collision](structural-season-id-collision.md): distinguish
  scoped season values from true duplicate season bridges.
- [Second-order bridge rejection](second-order-bridge-rejection.md): keep hub-derived
  bridges as candidates until the target provider is confirmed.
- [Local mirror staleness](local-mirror-staleness.md): prevent stale fast-read mirrors
  from re-proposing already-written bridges.
- [Duplicate player merge](duplicate-player-merge.md): tombstone, redirect, bridge
  movement, and conflict preservation.
- [Snapshot drift report](snapshot-drift-report.md): what to inspect before accepting a
  provider refresh.

## Longer Case Studies

- [Bridge conflict case study](bridge-conflict-case-study.md): a new source disagrees
  with a stronger existing bridge.
- [Duplicate merge with provider conflict](duplicate-merge-with-provider-conflict.md):
  same real player, but conflicting same-provider IDs block automatic data movement.
- [Provider ingest walkthrough](provider-ingest-walkthrough.md): provider card to
  snapshot to candidate output to write set.
