-- Reep Toolkit reference register schema.
-- Status: draft.
-- Public-safe: true.
-- Last verified: 2026-04-29.
--
-- This is an optional SQLite-shaped schema for examples and small deployments.
-- It is not a claim that every register must use these table or column names.

CREATE TABLE IF NOT EXISTS entities (
  entity_id TEXT PRIMARY KEY,
  entity_type TEXT NOT NULL CHECK (
    entity_type IN ('player', 'team', 'coach', 'competition', 'season', 'match')
  ),
  name TEXT NOT NULL,
  aliases TEXT,
  date_of_birth TEXT,
  country TEXT,
  nationality TEXT,
  position TEXT,
  parent_entity_id TEXT,
  canonical_entity_id TEXT,
  source TEXT,
  deleted_at TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS provider_ids (
  entity_id TEXT NOT NULL,
  provider TEXT NOT NULL,
  external_id TEXT NOT NULL,
  entity_type TEXT,
  source TEXT NOT NULL,
  confidence REAL NOT NULL,
  method TEXT NOT NULL,
  source_snapshot TEXT,
  matcher_version TEXT,
  review_status TEXT NOT NULL DEFAULT 'auto_accepted',
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (entity_id, provider, external_id)
);

CREATE INDEX IF NOT EXISTS idx_provider_ids_lookup
  ON provider_ids(provider, external_id);

CREATE TABLE IF NOT EXISTS aliases (
  entity_id TEXT NOT NULL,
  alias TEXT NOT NULL,
  provider TEXT,
  language TEXT,
  source_snapshot TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (entity_id, alias)
);

CREATE TABLE IF NOT EXISTS matches (
  entity_id TEXT PRIMARY KEY,
  match_date TEXT NOT NULL,
  kickoff_utc TEXT,
  home_team_id TEXT NOT NULL,
  away_team_id TEXT NOT NULL,
  competition_id TEXT,
  season_id TEXT,
  round_label TEXT,
  venue TEXT,
  source TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_matches_date_teams
  ON matches(match_date, home_team_id, away_team_id);

CREATE INDEX IF NOT EXISTS idx_matches_competition_date
  ON matches(competition_id, match_date);

CREATE TABLE IF NOT EXISTS match_decisions (
  decision_id TEXT PRIMARY KEY,
  provider TEXT NOT NULL,
  external_id TEXT NOT NULL,
  proposed_entity_id TEXT,
  entity_type TEXT NOT NULL,
  confidence REAL NOT NULL,
  method TEXT NOT NULL,
  source_snapshot TEXT,
  matcher_version TEXT,
  decision TEXT NOT NULL CHECK (
    decision IN ('accepted', 'rejected', 'needs_more_evidence', 'new_entity_candidate')
  ),
  reviewer TEXT,
  notes TEXT,
  decided_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
