CREATE TABLE project_orgs (
            id                  TEXT PRIMARY KEY,
            name                TEXT NOT NULL,
            slug                TEXT NOT NULL,
            org_key             TEXT NOT NULL,
            source              TEXT NOT NULL DEFAULT 'local',
            sync_provider       TEXT NOT NULL DEFAULT 'none',
            sync_config_json    TEXT,
            sync_connection_id  TEXT,
            external_org_id     TEXT,
            created_at          INTEGER NOT NULL,
            updated_at          INTEGER NOT NULL
        );
CREATE UNIQUE INDEX idx_project_orgs_slug ON project_orgs(slug);
CREATE UNIQUE INDEX idx_project_orgs_key ON project_orgs(org_key);
CREATE INDEX idx_project_orgs_source ON project_orgs(source);
CREATE TABLE projects (
            id                  TEXT PRIMARY KEY,
            org_id              TEXT NOT NULL DEFAULT 'personal-org' REFERENCES project_orgs(id) ON DELETE RESTRICT,
            name                TEXT NOT NULL,
            slug                TEXT NOT NULL,
            status              TEXT NOT NULL DEFAULT 'active',
            priority            TEXT NOT NULL DEFAULT 'none',
            health              TEXT NOT NULL DEFAULT 'on_track',
            lead                TEXT,
            description         TEXT,
            short_id_prefix     TEXT NOT NULL,
            next_work_item_id   INTEGER NOT NULL DEFAULT 1,
            start_date          TEXT,
            target_date         TEXT,
            linked_repos_json   TEXT NOT NULL DEFAULT '[]',
            agent_defaults_json TEXT,
            created_at          INTEGER NOT NULL,
            updated_at          INTEGER NOT NULL,
            local_version       INTEGER NOT NULL DEFAULT 0,
            sync_kind           TEXT NOT NULL DEFAULT 'none',
            sync_config_json    TEXT,
            sync_connection_id  TEXT,
            sync_last_pull_at   INTEGER,
            sync_cursor_blob    TEXT,
            sync_last_webhook_at INTEGER
        , collab_remote_version INTEGER, field_revisions_json TEXT);
CREATE UNIQUE INDEX idx_projects_slug ON projects(slug);
CREATE INDEX idx_projects_org ON projects(org_id);
CREATE INDEX idx_projects_status ON projects(status);
CREATE TABLE workitems (
            id                TEXT PRIMARY KEY,
            org_id            TEXT NOT NULL DEFAULT 'personal-org' REFERENCES project_orgs(id) ON DELETE RESTRICT,
            project_id          TEXT REFERENCES projects(id) ON DELETE SET NULL,
            short_id          TEXT NOT NULL,
            title             TEXT NOT NULL,
            body              TEXT NOT NULL DEFAULT '',
            status            TEXT NOT NULL DEFAULT 'backlog',
            priority          TEXT NOT NULL DEFAULT 'none',
            assigned_human_id TEXT,
            assignee          TEXT,
            assignee_type     TEXT,
            milestone         TEXT,
            parent            TEXT,
            start_date        TEXT,
            target_date       TEXT,
            estimate          REAL,
            order_index       INTEGER NOT NULL DEFAULT 0,
            created_at        INTEGER NOT NULL,
            updated_at        INTEGER NOT NULL,
            completed_at      INTEGER,
            deleted_at         INTEGER,
            local_version     INTEGER NOT NULL DEFAULT 0
        , collab_remote_version INTEGER);
CREATE UNIQUE INDEX idx_workitems_project_short_id
            ON workitems(project_id, short_id)
            WHERE project_id IS NOT NULL;
CREATE UNIQUE INDEX idx_workitems_standalone_short_id
            ON workitems(org_id, short_id)
            WHERE project_id IS NULL;
CREATE INDEX idx_workitems_org ON workitems(org_id);
CREATE INDEX idx_workitems_org_status
            ON workitems(org_id, status);
CREATE INDEX idx_workitems_project_status
            ON workitems(project_id, status);
CREATE INDEX idx_workitems_assigned_human ON workitems(assigned_human_id);
CREATE INDEX idx_workitems_assignee ON workitems(assignee);
CREATE INDEX idx_workitems_parent ON workitems(parent);
CREATE INDEX idx_workitems_milestone ON workitems(milestone);
CREATE INDEX idx_workitems_updated_at ON workitems(updated_at);
CREATE TABLE workitem_extras (
            work_item_id  TEXT PRIMARY KEY REFERENCES workitems(id) ON DELETE CASCADE,
            extras_json   TEXT NOT NULL DEFAULT '{}'
        );
CREATE TABLE workitem_labels (
            work_item_id  TEXT NOT NULL REFERENCES workitems(id) ON DELETE CASCADE,
            label_id      TEXT NOT NULL,
            PRIMARY KEY (work_item_id, label_id)
        );
CREATE INDEX idx_workitem_labels_label ON workitem_labels(label_id);
CREATE TABLE labels (
            id            TEXT NOT NULL,
            project_id    TEXT NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
            name          TEXT NOT NULL,
            color         TEXT,
            description   TEXT,
            created_at    INTEGER NOT NULL,
            PRIMARY KEY (project_id, id)
        );
CREATE UNIQUE INDEX idx_labels_project_name
            ON labels(project_id, name);
CREATE TABLE milestones (
            id            TEXT NOT NULL,
            project_id    TEXT NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
            name          TEXT NOT NULL,
            description   TEXT,
            target_date   TEXT,
            status        TEXT NOT NULL DEFAULT 'open',
            created_at    INTEGER NOT NULL,
            PRIMARY KEY (project_id, id)
        );
CREATE UNIQUE INDEX idx_milestones_project_name
            ON milestones(project_id, name);
CREATE TABLE members (
            id            TEXT NOT NULL,
            project_id    TEXT NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
            display_name  TEXT NOT NULL,
            email         TEXT,
            avatar_url    TEXT,
            kind          TEXT NOT NULL DEFAULT 'member', -- member | agent | org
            extras_json   TEXT,
            created_at    INTEGER NOT NULL,
            PRIMARY KEY (project_id, id)
        );
CREATE INDEX idx_members_project ON members(project_id);
CREATE TABLE routine_definitions (
            id                       TEXT PRIMARY KEY,
            name                     TEXT NOT NULL,
            description              TEXT NOT NULL DEFAULT '',
            enabled                  INTEGER NOT NULL DEFAULT 1,
            trigger_json             TEXT NOT NULL,
            run_template_json        TEXT NOT NULL,
            output_policy_json       TEXT NOT NULL DEFAULT '{}',
            created_at               INTEGER NOT NULL,
            updated_at               INTEGER NOT NULL
        , last_evaluated_at INTEGER, next_fire_at INTEGER);
CREATE INDEX idx_routine_definitions_enabled
            ON routine_definitions(enabled);
CREATE INDEX idx_routine_definitions_updated_at
            ON routine_definitions(updated_at);
CREATE TABLE routine_fires (
            id                  TEXT PRIMARY KEY,
            routine_id          TEXT NOT NULL REFERENCES routine_definitions(id) ON DELETE CASCADE,
            fired_at            INTEGER NOT NULL,
            status              TEXT NOT NULL,
            session_id          TEXT,
            agent_org_run_id    TEXT,
            work_item_id        TEXT,
            coalesced_into_fire_id TEXT,
            idempotency_key     TEXT,
            started_at          INTEGER,
            completed_at        INTEGER,
            error               TEXT
        );
CREATE INDEX idx_routine_fires_routine_id
            ON routine_fires(routine_id, fired_at DESC);
CREATE INDEX idx_routine_fires_session
            ON routine_fires(session_id);
CREATE INDEX idx_workitems_deleted_at ON workitems(deleted_at);
CREATE INDEX idx_routine_fires_work_item ON routine_fires(work_item_id);
CREATE UNIQUE INDEX idx_routine_fires_idempotency ON routine_fires(idempotency_key) WHERE idempotency_key IS NOT NULL;
CREATE INDEX idx_routine_fires_status ON routine_fires(routine_id, status, fired_at DESC);
CREATE TABLE outbox_entries (
            id                 INTEGER PRIMARY KEY AUTOINCREMENT,
            project_slug       TEXT NOT NULL,
            entity_type        TEXT NOT NULL,                  -- work_item | project | label | milestone | member
            entity_id          TEXT NOT NULL,                  -- short_id for work items, slug for projects, …
            op                 TEXT NOT NULL,                  -- create | update | delete | merge_external
            field_path         TEXT,                           -- dotted path within entity (NULL for create/delete)
            payload_json       TEXT NOT NULL DEFAULT '{}',
            created_at         INTEGER NOT NULL,               -- unix ms
            retry_count        INTEGER NOT NULL DEFAULT 0,
            last_attempted_at  INTEGER,
            last_error         TEXT,
            status             TEXT NOT NULL DEFAULT 'pending' -- pending | in_flight | succeeded | failed | abandoned
        , org_id TEXT);
CREATE TABLE sqlite_sequence(name,seq);
CREATE INDEX idx_outbox_status_created
            ON outbox_entries(status, created_at);
CREATE INDEX idx_outbox_project_entity
            ON outbox_entries(project_slug, entity_type, entity_id);
CREATE TABLE webhook_secrets (
            project_slug    TEXT NOT NULL,
            adapter_id      TEXT NOT NULL,
            secret_hex      TEXT NOT NULL,           -- 64 hex chars (32 bytes)
            last_rotated_at INTEGER NOT NULL,        -- unix ms
            PRIMARY KEY (project_slug, adapter_id)
        );
CREATE TABLE import_progress (
            project_slug    TEXT NOT NULL,
            adapter_id      TEXT NOT NULL,
            state           TEXT NOT NULL,           -- pending|running|completed|cancelled|failed
            page_cursor     TEXT,                    -- adapter-defined opaque cursor (NULL on first page)
            imported_count  INTEGER NOT NULL DEFAULT 0,
            total_hint      INTEGER,                 -- NULL when the adapter can't supply a count
            started_at      INTEGER NOT NULL,        -- unix ms (when the row was first created)
            updated_at      INTEGER NOT NULL,        -- unix ms (when last advanced)
            last_error      TEXT,                    -- non-NULL only when state='failed'
            PRIMARY KEY (project_slug, adapter_id)
        );
CREATE INDEX idx_import_progress_state
            ON import_progress(state);
CREATE TABLE outbox_conflicts (
            id                INTEGER PRIMARY KEY AUTOINCREMENT,
            project_slug      TEXT NOT NULL,
            adapter_id        TEXT NOT NULL,
            entity_type       TEXT NOT NULL,        -- mirrors EntityType enum (work_item|...)
            entity_id         TEXT NOT NULL,        -- short_id of the local row
            external_id       TEXT NOT NULL,        -- adapter's identifier for the remote row
            fields_json       TEXT NOT NULL,        -- ConflictFieldsPayload (typed)
            detected_at       INTEGER NOT NULL,     -- unix ms when the resolver flagged it
            resolved_at       INTEGER,              -- unix ms; NULL while open
            resolution        TEXT,                 -- use_local|use_remote|dismissed when set
            source_outbox_id  INTEGER               -- merge_external row id; NULL after that row is GC'd
        );
CREATE INDEX idx_outbox_conflicts_open
            ON outbox_conflicts(project_slug, resolved_at);
CREATE INDEX idx_outbox_conflicts_entity
            ON outbox_conflicts(project_slug, entity_id);
CREATE TABLE linear_metadata_cache (
            connection_id TEXT NOT NULL,
            scope         TEXT NOT NULL,
            scope_id      TEXT NOT NULL,
            payload_json  TEXT NOT NULL,
            fetched_at    INTEGER NOT NULL,
            expires_at    INTEGER NOT NULL,
            PRIMARY KEY (connection_id, scope, scope_id)
        );
CREATE INDEX idx_linear_metadata_cache_expires
            ON linear_metadata_cache(expires_at);
CREATE INDEX idx_outbox_org_status
             ON outbox_entries(org_id, status, created_at);
CREATE TABLE team_inbox_read_receipts (
            viewer_member_id TEXT NOT NULL,
            source_kind      TEXT NOT NULL,
            source_id        TEXT NOT NULL,
            read_at          INTEGER NOT NULL,
            PRIMARY KEY (viewer_member_id, source_kind, source_id)
        );
CREATE INDEX idx_team_inbox_receipts_source
            ON team_inbox_read_receipts(source_kind, source_id);
