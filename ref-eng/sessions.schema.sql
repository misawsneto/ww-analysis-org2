CREATE TABLE events (
            id TEXT PRIMARY KEY,
            session_id TEXT NOT NULL,
            event_type TEXT NOT NULL,
            function_name TEXT,
            thread_id TEXT,
            args_json TEXT NOT NULL DEFAULT '{}',
            result_json TEXT NOT NULL DEFAULT '{}',
            content TEXT NOT NULL DEFAULT '',
            created_at TEXT NOT NULL,
            meta_json TEXT,
            history_sequence INTEGER,
            UNIQUE(id, session_id)
        );
CREATE INDEX idx_events_session_id ON events(session_id);
CREATE INDEX idx_events_created_at ON events(created_at);
CREATE INDEX idx_events_session_created ON events(session_id, created_at);
CREATE INDEX idx_events_session_sequence ON events(session_id, history_sequence);
CREATE TABLE session_turns (
            session_id TEXT NOT NULL,
            turn_id TEXT NOT NULL,
            start_sequence INTEGER NOT NULL,
            end_sequence INTEGER,
            next_turn_id TEXT,
            started_at TEXT NOT NULL,
            ended_at TEXT,
            duration_ms INTEGER,
            user_event_ids_json TEXT NOT NULL DEFAULT '[]',
            user_preview TEXT NOT NULL DEFAULT '',
            event_count INTEGER NOT NULL DEFAULT 0,
            body_event_count INTEGER NOT NULL DEFAULT 0,
            status TEXT NOT NULL,
            interrupted INTEGER NOT NULL DEFAULT 0,
            updated_at TEXT NOT NULL, modified_files_json TEXT NOT NULL DEFAULT '[]', resource_interactions_json TEXT NOT NULL DEFAULT '[]', git_artifacts_json TEXT NOT NULL DEFAULT '[]',
            PRIMARY KEY (session_id, turn_id)
        );
CREATE INDEX idx_session_turns_session_sequence
         ON session_turns(session_id, start_sequence);
CREATE INDEX idx_session_turns_started_at
         ON session_turns(started_at);
CREATE TABLE session_turn_index_state (
            session_id TEXT PRIMARY KEY,
            indexed_event_count INTEGER NOT NULL,
            indexed_max_sequence INTEGER,
            rebuilt_at TEXT NOT NULL,
            index_version INTEGER NOT NULL DEFAULT 1
        );
CREATE TABLE session_turn_intents (
            session_id        TEXT NOT NULL,
            turn_intent_id    TEXT NOT NULL,
            client_message_id TEXT,
            source            TEXT NOT NULL,
            status            TEXT NOT NULL,
            created_at        TEXT NOT NULL,
            updated_at        TEXT NOT NULL, org_run_id TEXT,
            PRIMARY KEY (session_id, turn_intent_id)
        );
CREATE INDEX idx_session_turn_intents_session_status
         ON session_turn_intents(session_id, status);
CREATE TABLE sessions (
            session_id TEXT PRIMARY KEY,
            event_count INTEGER NOT NULL DEFAULT 0,
            cached_at INTEGER NOT NULL,
            time_range_start TEXT,
            time_range_end TEXT,
            specs_json TEXT
        );
CREATE TABLE session_token_usage (
            id                 INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id         TEXT NOT NULL,
            session_type       TEXT NOT NULL,
            model              TEXT,
            account_id         TEXT,
            input_tokens       INTEGER NOT NULL DEFAULT 0,
            output_tokens      INTEGER NOT NULL DEFAULT 0,
            cache_read_tokens  INTEGER NOT NULL DEFAULT 0,
            cache_write_tokens INTEGER NOT NULL DEFAULT 0,
            total_tokens       INTEGER NOT NULL DEFAULT 0,
            created_at         TEXT NOT NULL
        , context_tokens INTEGER NOT NULL DEFAULT 0, context_usage_json TEXT);
CREATE TABLE sqlite_sequence(name,seq);
CREATE INDEX idx_stu_session_id ON session_token_usage(session_id);
CREATE TABLE repos (
            repo_id    TEXT PRIMARY KEY,
            name       TEXT NOT NULL,
            path       TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        , visibility TEXT, kind TEXT DEFAULT 'git');
CREATE UNIQUE INDEX idx_repos_path ON repos(path);
CREATE TABLE workspaces (
            workspace_id    TEXT PRIMARY KEY,
            name            TEXT NOT NULL,
            primary_repo_id TEXT,
            created_at      TEXT NOT NULL,
            updated_at      TEXT NOT NULL
        );
CREATE TABLE workspace_folders (
            workspace_id TEXT NOT NULL,
            folder_path  TEXT NOT NULL,
            folder_name  TEXT NOT NULL,
            sort_order   INTEGER NOT NULL DEFAULT 0,
            is_primary   INTEGER NOT NULL DEFAULT 0,
            repo_id      TEXT,
            kind         TEXT DEFAULT 'git',
            PRIMARY KEY (workspace_id, folder_path),
            FOREIGN KEY (workspace_id) REFERENCES workspaces(workspace_id) ON DELETE CASCADE
        );
CREATE TABLE learnings (
            id                    TEXT PRIMARY KEY,
            agent_scope           TEXT NOT NULL DEFAULT '_global',
            content               TEXT NOT NULL,
            takeaway              TEXT,
            category              TEXT NOT NULL DEFAULT 'pattern',
            importance            REAL NOT NULL DEFAULT 0.5,
            confidence            REAL NOT NULL DEFAULT 0.5,
            embedding             BLOB,
            embedding_model       TEXT,

            -- Lifecycle
            status                TEXT NOT NULL DEFAULT 'pending',
            content_hash          TEXT,
            reinforcement_count   INTEGER NOT NULL DEFAULT 1,
            source                TEXT NOT NULL DEFAULT 'reflection',
            account_id            TEXT,

            -- Evolution DAG
            evolution_type        TEXT NOT NULL DEFAULT 'original',
            parent_id             TEXT,

            -- Tracking
            last_recalled_at      TEXT,

            -- Metadata
            source_session_id     TEXT,
            created_at            TEXT NOT NULL,
            updated_at            TEXT NOT NULL,

            FOREIGN KEY (parent_id) REFERENCES learnings(id)
        );
CREATE INDEX idx_learnings_scope
            ON learnings(agent_scope);
CREATE INDEX idx_learnings_category
            ON learnings(agent_scope, category);
CREATE INDEX idx_learnings_parent
            ON learnings(parent_id);
CREATE INDEX idx_learnings_hash ON learnings(content_hash);
CREATE INDEX idx_learnings_status ON learnings(status);
CREATE INDEX idx_learnings_account ON learnings(account_id, status);
CREATE TABLE consolidation_runs (
            id              TEXT PRIMARY KEY,
            agent_scope     TEXT NOT NULL,
            account_id      TEXT,
            trigger         TEXT NOT NULL,   -- 'idle' | 'lazy' | 'forced' | 'manual'
            mode            TEXT NOT NULL,   -- 'embedding' | 'manifest'
            pending_input   INTEGER NOT NULL DEFAULT 0,
            added           INTEGER NOT NULL DEFAULT 0,
            updated         INTEGER NOT NULL DEFAULT 0,
            deleted         INTEGER NOT NULL DEFAULT 0,
            none_count      INTEGER NOT NULL DEFAULT 0,
            abandoned       INTEGER NOT NULL DEFAULT 0,
            reinforced      INTEGER NOT NULL DEFAULT 0,
            error           TEXT,
            started_at      TEXT NOT NULL,
            finished_at     TEXT NOT NULL
        );
CREATE INDEX idx_consolidation_runs_scope
            ON consolidation_runs(agent_scope, finished_at DESC);
CREATE TABLE reflection_blacklist (
            account_id      TEXT NOT NULL,
            model_id        TEXT NOT NULL,
            error           TEXT,
            failed_at       TEXT NOT NULL,
            PRIMARY KEY (account_id, model_id)
        );
CREATE TABLE agent_sessions (
            session_id  TEXT PRIMARY KEY,
            name        TEXT NOT NULL DEFAULT '',
            status      TEXT NOT NULL DEFAULT 'idle',
            model       TEXT,
            account_id  TEXT,
            workspace_path TEXT,
            user_input  TEXT,
            created_at  TEXT NOT NULL,
            updated_at  TEXT NOT NULL
        , org_id TEXT, project_id TEXT, project_name TEXT, work_item_id TEXT, agent_role TEXT, worktree_path TEXT, worktree_branch TEXT, base_branch TEXT, merge_status TEXT, project_slug TEXT, agent_definition_id TEXT, org_member_id TEXT, key_source TEXT NOT NULL DEFAULT 'own_key', sm_content TEXT, sm_last_msg_idx INTEGER, last_turn_cancelled INTEGER NOT NULL DEFAULT 0, agent_exec_mode TEXT, draft_text TEXT, reply_target_event_id TEXT, session_type TEXT NOT NULL DEFAULT 'agent', channel TEXT, chat_id TEXT, parent_session_id TEXT, parent_event_id TEXT, workspace_additional_json TEXT NOT NULL DEFAULT '{}', native_harness_type TEXT, pinned INTEGER NOT NULL DEFAULT 0, last_terminal_turn_id TEXT, last_terminal_turn_status TEXT, last_terminal_turn_at TEXT);
CREATE TABLE agent_messages (
            id          TEXT PRIMARY KEY,
            session_id  TEXT NOT NULL,
            role        TEXT NOT NULL,
            content     TEXT NOT NULL DEFAULT '',
            tool_name   TEXT,
            tool_call_id TEXT,
            tool_input  TEXT,
            tool_output TEXT,
            model       TEXT,
            sequence    INTEGER NOT NULL,
            created_at  TEXT NOT NULL,
            -- Compact boundary pointer: NULL for ordinary rows. A non-NULL
            -- value marks this row as a compaction summary whose visible
            -- tail starts at that sequence. Rows are never rewritten or
            -- deleted by compaction (immutable transcript invariant).
            compact_from_sequence INTEGER
        , images TEXT, compact_tokens_before INTEGER, compact_tokens_after INTEGER);
CREATE INDEX idx_am_session
            ON agent_messages(session_id, sequence);
CREATE TABLE agent_snapshots (
            id           TEXT PRIMARY KEY,
            session_id   TEXT NOT NULL,
            tool_call_id TEXT NOT NULL,
            hash         TEXT NOT NULL,
            created_at   TEXT NOT NULL
        );
CREATE INDEX idx_as_session
            ON agent_snapshots(session_id, created_at);
CREATE TABLE agent_todos (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id  TEXT NOT NULL,
            content     TEXT NOT NULL,
            status      TEXT NOT NULL DEFAULT 'pending',
            priority    TEXT NOT NULL DEFAULT 'medium',
            position    INTEGER NOT NULL DEFAULT 0
        , active_form TEXT, blocked_by TEXT NOT NULL DEFAULT '[]');
CREATE INDEX idx_at_session
            ON agent_todos(session_id, position);
CREATE TABLE agent_file_resolutions (
            session_id  TEXT NOT NULL,
            file_path   TEXT NOT NULL,
            resolution  TEXT NOT NULL,
            created_at  TEXT NOT NULL,
            PRIMARY KEY (session_id, file_path)
        );
CREATE INDEX idx_agent_sessions_type ON agent_sessions(session_type);
CREATE INDEX idx_agent_sessions_parent ON agent_sessions(parent_session_id);
CREATE TABLE code_sessions (
            session_id     TEXT PRIMARY KEY,
            name           TEXT NOT NULL DEFAULT 'Code Session',
            status         TEXT NOT NULL DEFAULT 'pending',
            flow           TEXT NOT NULL DEFAULT 'quick',
            runner         TEXT NOT NULL DEFAULT 'local',
            billing_mode   TEXT NOT NULL DEFAULT 'local',
            platform       TEXT,
            cli_agent_type TEXT,
            model          TEXT,
            tier           TEXT,
            account_id     TEXT,
            repo_path      TEXT,
            branch         TEXT,
            user_input     TEXT,
            proxy_token    TEXT,
            proxy_url      TEXT,
            proxy_port     INTEGER,
            error_message  TEXT,
            token_usage    TEXT,
            pid            INTEGER,
            cli_session_id TEXT,
            parent_session_id TEXT,
            org_member_id TEXT,
            org_id TEXT NOT NULL DEFAULT 'personal-org',
            project_id TEXT,
            project_name TEXT,
            project_slug TEXT,
            work_item_id TEXT,
            agent_role TEXT,
            created_at     TEXT NOT NULL,
            updated_at     TEXT NOT NULL
        , hosted_token TEXT, proxy_session_id TEXT, worktree_path TEXT, worktree_branch TEXT, base_branch TEXT, merge_status TEXT, background INTEGER NOT NULL DEFAULT 0, key_source TEXT NOT NULL DEFAULT 'own_key', agent_exec_mode TEXT, draft_text TEXT, reply_target_event_id TEXT, pinned INTEGER NOT NULL DEFAULT 0, additional_directories TEXT, transcript_source TEXT NOT NULL DEFAULT 'chunks');
CREATE TABLE code_session_chunks (
            chunk_id       TEXT PRIMARY KEY,
            session_id     TEXT NOT NULL REFERENCES code_sessions(session_id) ON DELETE CASCADE,
            action_type    TEXT NOT NULL,
            function       TEXT NOT NULL,
            args_json      TEXT NOT NULL DEFAULT '{}',
            result_json    TEXT NOT NULL DEFAULT '{}',
            thread_id      TEXT,
            process_id     TEXT,
            sequence       INTEGER NOT NULL,
            created_at     TEXT NOT NULL
        );
CREATE INDEX idx_code_chunks_session
            ON code_session_chunks(session_id, sequence);
CREATE TABLE code_session_cli_resume_state (
            session_id     TEXT NOT NULL REFERENCES code_sessions(session_id) ON DELETE CASCADE,
            profile_key    TEXT NOT NULL,
            cli_session_id TEXT NOT NULL,
            updated_at     TEXT NOT NULL,
            PRIMARY KEY (session_id, profile_key)
        );
CREATE TABLE code_session_history_mutations (
            session_id TEXT PRIMARY KEY REFERENCES code_sessions(session_id) ON DELETE CASCADE,
            epoch      INTEGER NOT NULL DEFAULT 0,
            reason     TEXT NOT NULL,
            mutated_at TEXT NOT NULL
        );
CREATE INDEX idx_code_sessions_parent_org_member
            ON code_sessions(parent_session_id, org_member_id);
CREATE TABLE _migrations (name TEXT PRIMARY KEY, applied_at TEXT NOT NULL);
CREATE TABLE inbox_messages (
            id          TEXT PRIMARY KEY,
            title       TEXT NOT NULL,
            preview     TEXT NOT NULL DEFAULT '',
            content     TEXT NOT NULL DEFAULT '',
            category    TEXT NOT NULL DEFAULT 'git',
            priority    TEXT NOT NULL DEFAULT 'none',
            status      TEXT NOT NULL DEFAULT 'unread',
            sender_name TEXT,
            metadata    TEXT NOT NULL DEFAULT '{}',
            labels      TEXT NOT NULL DEFAULT '[]',
            created_at  TEXT NOT NULL,
            updated_at  TEXT NOT NULL
        );
CREATE INDEX idx_inbox_status ON inbox_messages(status);
CREATE INDEX idx_inbox_category ON inbox_messages(category);
CREATE INDEX idx_inbox_created ON inbox_messages(created_at);
CREATE TABLE orgtrack_core_sessions (
                session_id          TEXT PRIMARY KEY,
                source              TEXT NOT NULL,
                source_session_id   TEXT NOT NULL,
                workspace_path      TEXT,
                title               TEXT NOT NULL,
                created_at          TEXT,
                updated_at          TEXT,
                completed_at        TEXT,
                branch              TEXT,
                payload_json        TEXT NOT NULL
            , parent_session_id TEXT, status TEXT);
CREATE INDEX idx_orgtrack_core_sessions_source
                ON orgtrack_core_sessions(source, source_session_id);
CREATE INDEX idx_orgtrack_core_sessions_workspace
                ON orgtrack_core_sessions(workspace_path);
CREATE TABLE orgtrack_core_activities (
                record_id       TEXT PRIMARY KEY,
                source          TEXT NOT NULL,
                session_id      TEXT,
                timestamp       TEXT NOT NULL,
                workspace_path  TEXT,
                file_path       TEXT,
                kind            TEXT NOT NULL,
                payload_json    TEXT NOT NULL
            );
CREATE INDEX idx_orgtrack_core_activities_session
                ON orgtrack_core_activities(session_id, timestamp);
CREATE INDEX idx_orgtrack_core_activities_workspace
                ON orgtrack_core_activities(workspace_path, timestamp);
CREATE TABLE orgtrack_core_file_changes (
                record_id       TEXT PRIMARY KEY,
                source          TEXT NOT NULL,
                session_id      TEXT NOT NULL,
                workspace_path  TEXT,
                file_path       TEXT NOT NULL,
                path_hash       TEXT NOT NULL,
                timestamp       INTEGER NOT NULL,
                payload_json    TEXT NOT NULL
            );
CREATE INDEX idx_orgtrack_core_file_changes_session
                ON orgtrack_core_file_changes(session_id, timestamp);
CREATE INDEX idx_orgtrack_core_file_changes_workspace
                ON orgtrack_core_file_changes(workspace_path, timestamp);
CREATE INDEX idx_orgtrack_core_file_changes_path
                ON orgtrack_core_file_changes(file_path, timestamp);
CREATE TABLE orgtrack_core_commit_links (
                record_id       TEXT PRIMARY KEY,
                commit_sha      TEXT NOT NULL,
                linked_at       TEXT NOT NULL,
                payload_json    TEXT NOT NULL
            );
CREATE INDEX idx_orgtrack_core_commit_links_sha
                ON orgtrack_core_commit_links(commit_sha);
CREATE TABLE orgtrack_core_checkpoints (
                source          TEXT PRIMARY KEY,
                parser_version  INTEGER NOT NULL,
                updated_at      TEXT,
                payload_json    TEXT NOT NULL
            );
CREATE TABLE orgtrack_core_edit_artifacts (
                record_id       TEXT PRIMARY KEY,
                source          TEXT NOT NULL,
                session_id      TEXT NOT NULL,
                source_event_id TEXT,
                sequence_index  INTEGER NOT NULL,
                workspace_path  TEXT,
                file_path       TEXT NOT NULL,
                path_hash       TEXT NOT NULL,
                quality         TEXT NOT NULL,
                payload_json    TEXT NOT NULL
            );
CREATE INDEX idx_orgtrack_core_edit_artifacts_session
                ON orgtrack_core_edit_artifacts(source, session_id, sequence_index);
CREATE INDEX idx_orgtrack_core_edit_artifacts_workspace
                ON orgtrack_core_edit_artifacts(workspace_path, sequence_index);
CREATE INDEX idx_orgtrack_core_edit_artifacts_path
                ON orgtrack_core_edit_artifacts(file_path, sequence_index);
CREATE TABLE orgtrack_core_diff_chunks (
                record_id       TEXT PRIMARY KEY,
                edit_record_id  TEXT NOT NULL,
                source          TEXT NOT NULL,
                session_id      TEXT NOT NULL,
                source_event_id TEXT,
                sequence_index  INTEGER NOT NULL,
                chunk_index     INTEGER NOT NULL,
                file_path       TEXT NOT NULL,
                quality         TEXT NOT NULL,
                payload_json    TEXT NOT NULL
            );
CREATE INDEX idx_orgtrack_core_diff_chunks_session
                ON orgtrack_core_diff_chunks(source, session_id, sequence_index, chunk_index);
CREATE INDEX idx_orgtrack_core_diff_chunks_edit
                ON orgtrack_core_diff_chunks(edit_record_id);
CREATE TABLE orgtrack_core_final_diffs (
                record_id       TEXT PRIMARY KEY,
                source          TEXT NOT NULL,
                session_id      TEXT NOT NULL,
                file_path       TEXT NOT NULL,
                quality         TEXT NOT NULL,
                computed_at     TEXT NOT NULL,
                payload_json    TEXT NOT NULL
            );
CREATE INDEX idx_orgtrack_core_final_diffs_session
                ON orgtrack_core_final_diffs(source, session_id, file_path);
CREATE TABLE orgtrack_core_session_checkpoints (
                checkpoint_id   TEXT PRIMARY KEY,
                source          TEXT NOT NULL,
                session_id      TEXT NOT NULL,
                sequence_index  INTEGER NOT NULL,
                source_event_id TEXT,
                checkpoint_kind TEXT NOT NULL,
                quality         TEXT NOT NULL,
                undo_supported  INTEGER NOT NULL,
                payload_json    TEXT NOT NULL
            );
CREATE INDEX idx_orgtrack_core_session_checkpoints_session
                ON orgtrack_core_session_checkpoints(source, session_id, sequence_index);
CREATE TABLE orgtrack_core_checkpoint_file_states (
                record_id       TEXT PRIMARY KEY,
                checkpoint_id   TEXT NOT NULL,
                session_id      TEXT NOT NULL,
                file_path       TEXT NOT NULL,
                quality         TEXT NOT NULL,
                payload_json    TEXT NOT NULL
            );
CREATE INDEX idx_orgtrack_core_checkpoint_file_states_checkpoint
                ON orgtrack_core_checkpoint_file_states(checkpoint_id, file_path);
CREATE TABLE cursor_ide_turn_summaries (
                session_id          TEXT NOT NULL,
                composer_id         TEXT NOT NULL,
                turn_id             TEXT NOT NULL,
                next_turn_id        TEXT,
                turn_index          INTEGER NOT NULL,
                started_at          TEXT NOT NULL,
                ended_at            TEXT,
                duration_ms         INTEGER,
                user_preview        TEXT NOT NULL DEFAULT '',
                event_count         INTEGER NOT NULL DEFAULT 0,
                body_event_count    INTEGER NOT NULL DEFAULT 0,
                source_updated_at   INTEGER NOT NULL DEFAULT 0,
                source_bubble_count INTEGER NOT NULL DEFAULT 0,
                source_fingerprint  TEXT NOT NULL DEFAULT '',
                updated_at          TEXT NOT NULL,
                PRIMARY KEY (session_id, turn_id)
            );
CREATE INDEX idx_cursor_ide_turns_session_index
                ON cursor_ide_turn_summaries(session_id, turn_index);
CREATE TABLE claude_session_cache (
                id              TEXT PRIMARY KEY,
                name            TEXT NOT NULL DEFAULT '',
                created_at      INTEGER NOT NULL DEFAULT 0,
                last_active_at  INTEGER NOT NULL DEFAULT 0,
                message_count   INTEGER NOT NULL DEFAULT 0,
                model           TEXT NOT NULL DEFAULT '',
                workspace_path  TEXT NOT NULL DEFAULT '',
                git_branch      TEXT NOT NULL DEFAULT '',
                input_tokens    INTEGER NOT NULL DEFAULT 0,
                output_tokens   INTEGER NOT NULL DEFAULT 0
            );
CREATE INDEX idx_claude_cache_created
                ON claude_session_cache(created_at);
CREATE TABLE cli_session_cache (
                id              TEXT PRIMARY KEY,
                tool            TEXT NOT NULL DEFAULT '',
                name            TEXT NOT NULL DEFAULT '',
                created_at      INTEGER NOT NULL DEFAULT 0,
                last_active_at  INTEGER NOT NULL DEFAULT 0,
                message_count   INTEGER NOT NULL DEFAULT 0,
                model           TEXT NOT NULL DEFAULT '',
                workspace_path  TEXT NOT NULL DEFAULT '',
                input_tokens    INTEGER NOT NULL DEFAULT 0,
                output_tokens   INTEGER NOT NULL DEFAULT 0
            );
CREATE INDEX idx_cli_cache_created
                ON cli_session_cache(created_at);
CREATE INDEX idx_cli_cache_tool
                ON cli_session_cache(tool);
CREATE TABLE imported_history_session_cache (
                source              TEXT NOT NULL,
                source_session_id   TEXT NOT NULL,
                session_id          TEXT NOT NULL,
                source_path         TEXT NOT NULL DEFAULT '',
                source_record_key   TEXT NOT NULL DEFAULT '',
                source_mtime_ms     INTEGER NOT NULL DEFAULT 0,
                source_size_bytes   INTEGER NOT NULL DEFAULT 0,
                source_fingerprint  TEXT NOT NULL DEFAULT '',
                parser_version      INTEGER NOT NULL DEFAULT 0,
                name                TEXT NOT NULL DEFAULT '',
                created_at_ms       INTEGER NOT NULL DEFAULT 0,
                updated_at_ms       INTEGER NOT NULL DEFAULT 0,
                model               TEXT NOT NULL DEFAULT '',
                input_tokens        INTEGER NOT NULL DEFAULT 0,
                output_tokens       INTEGER NOT NULL DEFAULT 0,
                repo_path           TEXT NOT NULL DEFAULT '',
                branch              TEXT NOT NULL DEFAULT '',
                files_changed       INTEGER NOT NULL DEFAULT 0,
                lines_added         INTEGER NOT NULL DEFAULT 0,
                lines_removed       INTEGER NOT NULL DEFAULT 0,
                touched_files_json  TEXT NOT NULL DEFAULT '[]',
                listable            INTEGER NOT NULL DEFAULT 1,
                source_metadata_json TEXT NOT NULL DEFAULT '',
                updated_at          TEXT NOT NULL DEFAULT '', parent_session_id TEXT NOT NULL DEFAULT '', cache_read_tokens INTEGER NOT NULL DEFAULT 0, cache_write_tokens INTEGER NOT NULL DEFAULT 0,
                PRIMARY KEY (source, source_session_id)
            );
CREATE INDEX idx_imported_history_source_updated
                ON imported_history_session_cache(source, updated_at_ms DESC);
CREATE INDEX idx_imported_history_source_repo
                ON imported_history_session_cache(source, repo_path);
CREATE INDEX idx_imported_history_source_path
                ON imported_history_session_cache(source, source_path);
CREATE TABLE node_provenance (
            id INTEGER PRIMARY KEY,
            session_id TEXT NOT NULL,
            file TEXT NOT NULL,
            function_name TEXT,
            node_type TEXT,
            node_hash TEXT,
            start_line INTEGER NOT NULL,
            end_line INTEGER NOT NULL,
            created_at INTEGER NOT NULL
        );
CREATE INDEX idx_np_session ON node_provenance(session_id);
CREATE INDEX idx_np_file ON node_provenance(file);
CREATE INDEX idx_np_hash ON node_provenance(node_hash);
CREATE TABLE commit_lineage (
            id INTEGER PRIMARY KEY,
            provenance_id INTEGER NOT NULL,
            commit_id TEXT NOT NULL,
            file TEXT NOT NULL,
            created_at INTEGER NOT NULL
        );
CREATE UNIQUE INDEX idx_cl_prov_commit
            ON commit_lineage(provenance_id, commit_id);
CREATE INDEX idx_cl_commit ON commit_lineage(commit_id);
CREATE TABLE agent_org_runs (
            id TEXT PRIMARY KEY,
            org_id TEXT NOT NULL,
            coordinator_agent_id TEXT NOT NULL,
            root_session_id TEXT,
            org_snapshot_json TEXT,
            entry_mode TEXT NOT NULL,
            status TEXT NOT NULL,
            work_item_id TEXT,
            project_slug TEXT,
            routine_fire_id TEXT,
            summary TEXT,
            last_error TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            completed_at TEXT
        );
CREATE INDEX idx_agent_org_runs_org_updated
            ON agent_org_runs(org_id, updated_at);
CREATE INDEX idx_agent_org_runs_root_session
            ON agent_org_runs(root_session_id);
CREATE INDEX idx_agent_org_runs_work_item
            ON agent_org_runs(work_item_id);
CREATE INDEX idx_agent_org_runs_status
            ON agent_org_runs(status);
CREATE TABLE agent_inbox (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipient_agent_id TEXT NOT NULL,
            recipient_member_id TEXT,
            sender_agent_id TEXT NOT NULL,
            sender_member_id TEXT,
            org_run_id TEXT,
            payload_kind TEXT NOT NULL,
            payload_json TEXT NOT NULL,
            request_id TEXT,
            created_at TEXT NOT NULL,
            read_at TEXT
        , causation_inbox_id INTEGER, display_text TEXT);
CREATE INDEX idx_agent_inbox_recipient_member_unread
            ON agent_inbox(recipient_member_id, read_at, created_at);
CREATE INDEX idx_agent_inbox_recipient_unread
            ON agent_inbox(recipient_agent_id, read_at, created_at);
CREATE INDEX idx_agent_inbox_org_run
            ON agent_inbox(org_run_id, created_at);
CREATE INDEX idx_agent_inbox_request_id
            ON agent_inbox(request_id);
CREATE TABLE agent_org_tasks (
            id TEXT NOT NULL,
            org_run_id TEXT NOT NULL,
            subject TEXT NOT NULL,
            description TEXT NOT NULL DEFAULT '',
            active_form TEXT,
            owner TEXT,
            status TEXT NOT NULL,
            blocks_json TEXT NOT NULL DEFAULT '[]',
            blocked_by_json TEXT NOT NULL DEFAULT '[]',
            metadata_json TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            PRIMARY KEY (org_run_id, id)
        );
CREATE INDEX idx_agent_org_tasks_status
            ON agent_org_tasks(org_run_id, status, owner);
CREATE INDEX idx_agent_org_tasks_owner
            ON agent_org_tasks(org_run_id, owner);
CREATE TABLE agent_org_task_events (
            id TEXT PRIMARY KEY,
            org_run_id TEXT NOT NULL,
            task_id TEXT NOT NULL,
            event_type TEXT NOT NULL,
            previous_owner TEXT,
            next_owner TEXT,
            previous_status TEXT,
            next_status TEXT,
            actor_member_id TEXT,
            created_at TEXT NOT NULL
        );
CREATE INDEX idx_agent_org_task_events_run
            ON agent_org_task_events(org_run_id, created_at, id);
CREATE INDEX idx_agent_org_task_events_task
            ON agent_org_task_events(org_run_id, task_id, created_at, id);
CREATE TABLE agent_member_interventions (
            org_run_id TEXT NOT NULL,
            member_id TEXT NOT NULL,
            agent_id TEXT NOT NULL,
            session_id TEXT NOT NULL,
            status TEXT NOT NULL,
            reason TEXT,
            entered_at TEXT NOT NULL,
            last_user_activity_at TEXT NOT NULL,
            resume_after TEXT NOT NULL,
            cleared_at TEXT,
            PRIMARY KEY (org_run_id, member_id)
        );
CREATE INDEX idx_agent_member_interventions_session
            ON agent_member_interventions(session_id);
CREATE INDEX idx_agent_member_interventions_active
            ON agent_member_interventions(org_run_id, cleared_at, resume_after);
CREATE TABLE pending_plan_approvals (
            session_id    TEXT PRIMARY KEY,
            tool_call_id  TEXT,
            plan_id       TEXT,
            plan_revision_id TEXT,
            origin_tool_call_id TEXT,
            plan_path     TEXT NOT NULL,
            plan_title    TEXT NOT NULL,
            plan_content  TEXT NOT NULL,
            created_at    INTEGER NOT NULL
        ) WITHOUT ROWID;
CREATE TABLE goal_loop_state (
            session_id  TEXT PRIMARY KEY,
            goal_text   TEXT NOT NULL,
            turns_used  INTEGER NOT NULL DEFAULT 0,
            status      TEXT NOT NULL DEFAULT 'active',
            updated_at  INTEGER NOT NULL
        ) WITHOUT ROWID;
CREATE TABLE session_llm_usage_spans (
            id                         INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id                 TEXT NOT NULL,
            turn_id                    TEXT NOT NULL,
            iteration_index            INTEGER NOT NULL,
            model                      TEXT,
            account_id                 TEXT,
            prompt_tokens              INTEGER NOT NULL DEFAULT 0,
            completion_tokens          INTEGER NOT NULL DEFAULT 0,
            cache_read_tokens          INTEGER NOT NULL DEFAULT 0,
            cache_write_tokens         INTEGER NOT NULL DEFAULT 0,
            total_tokens               INTEGER NOT NULL DEFAULT 0,
            context_tokens             INTEGER NOT NULL DEFAULT 0,
            related_tool_call_ids_json TEXT,
            context_usage_json         TEXT,
            created_at                 TEXT NOT NULL
        );
CREATE INDEX idx_slus_session_turn ON session_llm_usage_spans(session_id, turn_id);
CREATE INDEX idx_slus_session_iteration ON session_llm_usage_spans(session_id, iteration_index);
CREATE TABLE session_tool_usage (
            id                         INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id                 TEXT NOT NULL,
            turn_id                    TEXT NOT NULL,
            event_id                   TEXT NOT NULL,
            tool_call_id               TEXT NOT NULL,
            tool_name                  TEXT NOT NULL,
            iteration_index            INTEGER NOT NULL,
            decision_completion_tokens INTEGER NOT NULL DEFAULT 0,
            result_context_tokens      INTEGER NOT NULL DEFAULT 0,
            followup_completion_tokens INTEGER NOT NULL DEFAULT 0,
            input_bytes                INTEGER NOT NULL DEFAULT 0,
            output_bytes               INTEGER NOT NULL DEFAULT 0,
            attribution_method         TEXT NOT NULL,
            created_at                 TEXT NOT NULL
        );
CREATE INDEX idx_stool_session_turn ON session_tool_usage(session_id, turn_id);
CREATE INDEX idx_stool_session_call ON session_tool_usage(session_id, tool_call_id);
CREATE INDEX idx_stool_session_iteration ON session_tool_usage(session_id, iteration_index);
CREATE TABLE orgtrack_session_impacts (
            session_id TEXT PRIMARY KEY,
            source TEXT NOT NULL,
            workspace_path TEXT,
            files_changed INTEGER NOT NULL DEFAULT 0,
            lines_added INTEGER NOT NULL DEFAULT 0,
            lines_removed INTEGER NOT NULL DEFAULT 0,
            touched_files_json TEXT NOT NULL DEFAULT '[]',
            commit_shas_json TEXT NOT NULL DEFAULT '[]',
            last_event_at TEXT,
            schema_version INTEGER NOT NULL DEFAULT 1,
            updated_at TEXT NOT NULL
         );
CREATE TABLE orgtrack_session_impact_events (
            event_id TEXT PRIMARY KEY,
            session_id TEXT NOT NULL,
            source TEXT NOT NULL,
            created_at TEXT NOT NULL
         );
CREATE INDEX idx_orgtrack_session_impact_events_session
            ON orgtrack_session_impact_events(session_id);
CREATE TABLE orgtrack_session_impact_backfills (
            session_id TEXT PRIMARY KEY,
            event_count INTEGER NOT NULL DEFAULT 0,
            completed_at TEXT NOT NULL
         );
CREATE TABLE shell_replays (
            session_id TEXT NOT NULL,
            call_id TEXT NOT NULL,
            relative_path TEXT NOT NULL,
            status TEXT NOT NULL,
            total_bytes INTEGER NOT NULL DEFAULT 0,
            last_sequence INTEGER NOT NULL DEFAULT 0,
            terminal_preview TEXT NOT NULL DEFAULT '',
            error TEXT,
            completed_at TEXT,
            format_version INTEGER NOT NULL DEFAULT 1,
            command TEXT NOT NULL DEFAULT '',
            cwd TEXT NOT NULL DEFAULT '',
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            PRIMARY KEY (session_id, call_id)
        );
CREATE INDEX idx_shell_replays_session
            ON shell_replays(session_id);
CREATE TABLE shell_replay_pages (
            session_id TEXT NOT NULL,
            call_id TEXT NOT NULL,
            page_index INTEGER NOT NULL,
            file_offset INTEGER NOT NULL,
            output_byte_start INTEGER NOT NULL,
            first_sequence INTEGER NOT NULL,
            last_sequence INTEGER NOT NULL DEFAULT 0,
            line_count INTEGER NOT NULL DEFAULT 0,
            PRIMARY KEY (session_id, call_id, page_index)
        );
CREATE INDEX idx_shell_replay_pages_lookup
            ON shell_replay_pages(session_id, call_id, output_byte_start);
CREATE TABLE shell_replay_cleanup_jobs (
            session_id TEXT NOT NULL,
            relative_path TEXT NOT NULL,
            attempts INTEGER NOT NULL DEFAULT 0,
            last_error TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            PRIMARY KEY (session_id, relative_path)
        );
CREATE INDEX idx_shell_replay_cleanup_session
            ON shell_replay_cleanup_jobs(session_id);
CREATE TABLE code_session_native_transcript_ids (
            session_id        TEXT NOT NULL,
            source            TEXT NOT NULL,
            source_session_id TEXT NOT NULL,
            bound_at          TEXT NOT NULL,
            PRIMARY KEY (session_id, source, source_session_id)
        );
CREATE INDEX idx_orgtrack_core_sessions_updated
                ON orgtrack_core_sessions(updated_at DESC);
CREATE TABLE orgtrack_core_resources (
                resource_id         TEXT PRIMARY KEY,
                resource_kind       TEXT NOT NULL,
                canonical_locator   TEXT NOT NULL,
                display_locator     TEXT NOT NULL,
                payload_json        TEXT NOT NULL
            );
CREATE INDEX idx_orgtrack_core_resources_locator
                ON orgtrack_core_resources(resource_kind, canonical_locator);
CREATE TABLE orgtrack_core_file_resources (
                resource_id         TEXT PRIMARY KEY,
                repository_id       TEXT,
                workspace_path      TEXT NOT NULL,
                repo_relative_path  TEXT NOT NULL,
                path_hash           TEXT NOT NULL,
                FOREIGN KEY(resource_id) REFERENCES orgtrack_core_resources(resource_id)
            );
CREATE INDEX idx_orgtrack_core_file_resources_repo
                ON orgtrack_core_file_resources(repository_id, repo_relative_path);
CREATE INDEX idx_orgtrack_core_file_resources_workspace
                ON orgtrack_core_file_resources(workspace_path, repo_relative_path);
CREATE TABLE orgtrack_core_resource_interactions (
                interaction_id       TEXT PRIMARY KEY,
                source               TEXT NOT NULL,
                source_session_id    TEXT,
                source_event_id      TEXT,
                session_id           TEXT NOT NULL,
                turn_id              TEXT,
                actor_id             TEXT,
                resource_id          TEXT NOT NULL,
                action               TEXT NOT NULL,
                outcome              TEXT NOT NULL,
                occurred_at          TEXT NOT NULL,
                capture_method       TEXT NOT NULL,
                attribution_precision TEXT NOT NULL,
                payload_json         TEXT NOT NULL,
                FOREIGN KEY(resource_id) REFERENCES orgtrack_core_resources(resource_id)
            );
CREATE INDEX idx_orgtrack_core_resource_interactions_resource
                ON orgtrack_core_resource_interactions(resource_id, occurred_at DESC);
CREATE INDEX idx_orgtrack_core_resource_interactions_session
                ON orgtrack_core_resource_interactions(session_id, occurred_at DESC);
CREATE INDEX idx_orgtrack_core_resource_interactions_observation
                ON orgtrack_core_resource_interactions(source, source_event_id, resource_id, action)
                WHERE source_event_id IS NOT NULL;
CREATE TABLE orgtrack_core_resource_revisions (
                resource_id  TEXT PRIMARY KEY,
                revision     INTEGER NOT NULL,
                updated_at   TEXT NOT NULL
            );
CREATE TRIGGER orgtrack_core_resource_revision_insert
            AFTER INSERT ON orgtrack_core_resource_interactions
            BEGIN
                INSERT INTO orgtrack_core_resource_revisions(resource_id, revision, updated_at)
                VALUES (NEW.resource_id, 1, NEW.occurred_at)
                ON CONFLICT(resource_id) DO UPDATE SET
                    revision = revision + 1,
                    updated_at = excluded.updated_at;
            END;
CREATE TRIGGER orgtrack_core_resource_revision_delete
            AFTER DELETE ON orgtrack_core_resource_interactions
            BEGIN
                INSERT INTO orgtrack_core_resource_revisions(resource_id, revision, updated_at)
                VALUES (OLD.resource_id, 1, strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
                ON CONFLICT(resource_id) DO UPDATE SET
                    revision = revision + 1,
                    updated_at = excluded.updated_at;
            END;
CREATE TABLE orgtrack_core_session_actors (
                actor_record_id        TEXT PRIMARY KEY,
                source                 TEXT NOT NULL,
                source_session_id      TEXT NOT NULL,
                session_id             TEXT NOT NULL,
                turn_id                TEXT,
                actor_id               TEXT NOT NULL,
                actor_type             TEXT,
                started_at             TEXT,
                stopped_at             TEXT,
                transcript_session_id  TEXT,
                transcript_path        TEXT,
                payload_json           TEXT NOT NULL,
                UNIQUE(source, source_session_id, actor_id)
            );
CREATE INDEX idx_orgtrack_core_session_actors_session
                ON orgtrack_core_session_actors(source, session_id, turn_id);
CREATE INDEX idx_orgtrack_core_session_actors_transcript
                ON orgtrack_core_session_actors(source, transcript_session_id)
                WHERE transcript_session_id IS NOT NULL;
CREATE TABLE orgtrack_core_interaction_import_checkpoints (
                source              TEXT NOT NULL,
                session_id          TEXT NOT NULL,
                source_fingerprint  TEXT NOT NULL,
                parser_version      INTEGER NOT NULL,
                reconciled_at       TEXT NOT NULL,
                PRIMARY KEY (source, session_id)
            );
CREATE TABLE orgtrack_core_interaction_backfill_jobs (
                repo_key            TEXT PRIMARY KEY,
                status              TEXT NOT NULL,
                indexed_sessions    INTEGER NOT NULL,
                total_sessions      INTEGER NOT NULL,
                failed_sessions     INTEGER NOT NULL,
                last_error          TEXT,
                run_token           TEXT NOT NULL,
                updated_at_ms       INTEGER NOT NULL
            );
CREATE TABLE orgtrack_core_session_usage (
                session_id          TEXT PRIMARY KEY,
                source              TEXT NOT NULL,
                model               TEXT,
                account_id          TEXT,
                key_source          TEXT,
                input_tokens        INTEGER NOT NULL DEFAULT 0,
                output_tokens       INTEGER NOT NULL DEFAULT 0,
                cache_read_tokens   INTEGER NOT NULL DEFAULT 0,
                cache_write_tokens  INTEGER NOT NULL DEFAULT 0,
                total_tokens        INTEGER NOT NULL DEFAULT 0,
                context_tokens      INTEGER NOT NULL DEFAULT 0,
                recorded_cost_usd   REAL NOT NULL DEFAULT 0,
                estimated_cost_usd  REAL NOT NULL DEFAULT 0,
                cost_usd            REAL NOT NULL DEFAULT 0,
                tokens_source       TEXT NOT NULL DEFAULT 'none',
                computed_at         TEXT NOT NULL
            );
CREATE INDEX idx_orgtrack_core_session_usage_model
                ON orgtrack_core_session_usage(model);
CREATE INDEX idx_orgtrack_core_session_usage_source
                ON orgtrack_core_session_usage(source);
CREATE INDEX idx_orgtrack_core_sessions_parent
             ON orgtrack_core_sessions(parent_session_id);
CREATE INDEX idx_imported_history_session_id
                ON imported_history_session_cache(session_id);
CREATE INDEX idx_imported_history_sidebar_order
                ON imported_history_session_cache(
                    source,
                    updated_at_ms DESC,
                    created_at_ms DESC,
                    source_session_id ASC
                )
                WHERE listable = 1 AND parent_session_id = '';
CREATE TABLE imported_history_round_usage (
                source             TEXT NOT NULL,
                source_session_id  TEXT NOT NULL,
                session_id         TEXT NOT NULL,
                seq                INTEGER NOT NULL,
                model              TEXT NOT NULL DEFAULT '',
                input_tokens       INTEGER NOT NULL DEFAULT 0,
                output_tokens      INTEGER NOT NULL DEFAULT 0,
                cache_read_tokens  INTEGER NOT NULL DEFAULT 0,
                cache_write_tokens INTEGER NOT NULL DEFAULT 0,
                created_at_ms      INTEGER NOT NULL DEFAULT 0,
                PRIMARY KEY (session_id, seq)
            );
CREATE INDEX idx_imported_round_session
                ON imported_history_round_usage(session_id);
CREATE INDEX idx_imported_round_created
                ON imported_history_round_usage(created_at_ms DESC);
CREATE INDEX idx_imported_round_source
                ON imported_history_round_usage(source);
CREATE TABLE agent_org_run_progress (
            org_run_id TEXT PRIMARY KEY,
            work_revision INTEGER NOT NULL DEFAULT 0 CHECK(work_revision >= 0),
            coordinator_presented_work_revision INTEGER,
            coordinator_observed_work_revision INTEGER,
            completion_requested INTEGER NOT NULL DEFAULT 0,
            completion_requested_at TEXT,
            completion_requested_work_revision INTEGER,
            completion_summary TEXT,
            updated_at TEXT NOT NULL,
            FOREIGN KEY(org_run_id) REFERENCES agent_org_runs(id) ON DELETE CASCADE
        );
CREATE TABLE agent_inbox_materializations (
            inbox_id INTEGER PRIMARY KEY,
            session_id TEXT NOT NULL,
            transcript_message_id TEXT NOT NULL,
            transcript_intent_id TEXT NOT NULL,
            materialized_at TEXT NOT NULL
        );
CREATE INDEX idx_agent_inbox_materializations_session
            ON agent_inbox_materializations(session_id, inbox_id);
CREATE INDEX idx_agent_inbox_org_run_id
            ON agent_inbox(org_run_id, id);
CREATE INDEX idx_agent_inbox_run_unread_recipient
            ON agent_inbox(org_run_id, recipient_member_id, recipient_agent_id, id)
            WHERE read_at IS NULL;
CREATE INDEX idx_agent_inbox_run_kind_id
            ON agent_inbox(org_run_id, payload_kind, id);
CREATE INDEX idx_agent_inbox_run_task_assignment_v4
            ON agent_inbox(
                org_run_id,
                recipient_member_id,
                json_extract(
                    CASE WHEN length(CAST(payload_json AS BLOB))<=262144
                                   AND json_valid(payload_json)
                         THEN payload_json ELSE '{}' END,
                    '$.task_id'
                )
            )
            WHERE payload_kind='task_assigned'
              AND CASE WHEN length(CAST(payload_json AS BLOB))<=262144
                       THEN json_valid(payload_json) ELSE 0 END
              AND json_type(
                    CASE WHEN length(CAST(payload_json AS BLOB))<=262144
                                   AND json_valid(payload_json)
                         THEN payload_json ELSE '{}' END,
                    '$.task_id'
                  )='text';
CREATE UNIQUE INDEX idx_agent_inbox_causation_recipient_once
            ON agent_inbox(
                causation_inbox_id,
                payload_kind,
                recipient_agent_id,
                COALESCE(recipient_member_id, '')
            )
            WHERE causation_inbox_id IS NOT NULL;
CREATE TABLE agent_org_plan_approvals (
            approval_id TEXT PRIMARY KEY,
            plan_revision_id TEXT NOT NULL UNIQUE,
            request_id TEXT NOT NULL UNIQUE,
            org_run_id TEXT NOT NULL,
            source_task_id TEXT NOT NULL,
            source_member_id TEXT NOT NULL,
            source_session_id TEXT NOT NULL,
            root_session_id TEXT NOT NULL,
            policy TEXT NOT NULL,
            status TEXT NOT NULL,
            plan_title TEXT NOT NULL,
            plan_path TEXT NOT NULL,
            plan_content TEXT NOT NULL,
            decision_by TEXT,
            feedback TEXT,
            created_at TEXT NOT NULL,
            resolved_at TEXT
        );
CREATE INDEX idx_agent_org_plan_approvals_run_status
            ON agent_org_plan_approvals(org_run_id, status, created_at);
CREATE INDEX idx_agent_org_plan_approvals_task
            ON agent_org_plan_approvals(org_run_id, source_task_id, created_at);
CREATE TABLE agent_org_recovery_attempts (
            org_run_id TEXT NOT NULL,
            action_kind TEXT NOT NULL,
            target_key TEXT NOT NULL,
            reason_fingerprint TEXT NOT NULL,
            attempts INTEGER NOT NULL DEFAULT 0,
            next_allowed_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            reservation_token TEXT,
            PRIMARY KEY (org_run_id, action_kind, target_key)
        );
CREATE INDEX idx_agent_org_recovery_attempts_run
            ON agent_org_recovery_attempts(org_run_id);
CREATE TABLE housekeeper_context_compaction (
            session_id TEXT PRIMARY KEY,
            enabled INTEGER NOT NULL DEFAULT 0,
            summary TEXT NOT NULL DEFAULT '',
            covered_message_count INTEGER NOT NULL DEFAULT 0,
            covered_prefix_hash TEXT NOT NULL DEFAULT '',
            source_tokens INTEGER NOT NULL DEFAULT 0,
            summary_tokens INTEGER NOT NULL DEFAULT 0,
            status TEXT NOT NULL DEFAULT 'disabled',
            last_error TEXT,
            last_run_at TEXT,
            updated_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
        );
CREATE INDEX idx_housekeeper_context_compaction_enabled
            ON housekeeper_context_compaction(enabled, last_run_at);
CREATE TABLE human_session_entries (
            id         TEXT PRIMARY KEY,
            session_id TEXT NOT NULL REFERENCES agent_sessions(session_id) ON DELETE CASCADE,
            body       TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
CREATE INDEX idx_human_session_entries_session
            ON human_session_entries(session_id, created_at);
CREATE TABLE imported_history_repo_identity (
                working_path          TEXT PRIMARY KEY,
                repo_root_path        TEXT NOT NULL DEFAULT '',
                remote_urls_json      TEXT NOT NULL DEFAULT '[]',
                resolution_kind       TEXT NOT NULL DEFAULT 'not_git',
                checked_at_ms         INTEGER NOT NULL DEFAULT 0,
                next_refresh_at_ms    INTEGER NOT NULL DEFAULT 0
            );
CREATE INDEX idx_imported_history_repo_identity_refresh
                ON imported_history_repo_identity(next_refresh_at_ms);
CREATE INDEX idx_imported_history_parent_created
                ON imported_history_session_cache(
                    source,
                    parent_session_id,
                    created_at_ms,
                    source_session_id
                )
                WHERE parent_session_id != '';
CREATE TABLE imported_history_parse_watermarks (
                source             TEXT NOT NULL,
                source_session_id  TEXT NOT NULL,
                byte_offset        INTEGER NOT NULL DEFAULT 0,
                source_size_bytes  INTEGER NOT NULL DEFAULT 0,
                source_mtime_ms    INTEGER NOT NULL DEFAULT 0,
                prefix_hash        TEXT NOT NULL DEFAULT '',
                parser_version     INTEGER NOT NULL DEFAULT 0,
                state_json         TEXT NOT NULL DEFAULT '',
                PRIMARY KEY (source, source_session_id)
            );
CREATE INDEX idx_session_turn_intents_org_run_status
         ON session_turn_intents(org_run_id, status)
         WHERE org_run_id IS NOT NULL;
CREATE TABLE imported_history_scan_snapshots (
                source            TEXT NOT NULL,
                directory_path    TEXT NOT NULL,
                dir_mtime_ns      INTEGER NOT NULL DEFAULT 0,
                file_count        INTEGER NOT NULL DEFAULT 0,
                snapshot_version  INTEGER NOT NULL DEFAULT 0,
                entries_json      TEXT NOT NULL DEFAULT '{}',
                PRIMARY KEY (source, directory_path)
            );
CREATE TABLE orgtrack_core_session_signals (
            session_id TEXT PRIMARY KEY,
            source TEXT NOT NULL,
            signals_version INTEGER NOT NULL,
            started_at_ms INTEGER NOT NULL DEFAULT 0,
            active_secs REAL NOT NULL DEFAULT 0,
            active_spans_json TEXT NOT NULL DEFAULT '[]',
            has_edit INTEGER NOT NULL DEFAULT 0,
            postedit_turns INTEGER NOT NULL DEFAULT 0,
            unreadable INTEGER NOT NULL DEFAULT 0,
            signals_json TEXT NOT NULL,
            computed_at TEXT NOT NULL
        );
CREATE INDEX idx_ocss_source ON orgtrack_core_session_signals(source);
CREATE INDEX idx_ocss_started ON orgtrack_core_session_signals(started_at_ms);
CREATE INDEX idx_ocss_version ON orgtrack_core_session_signals(signals_version);
CREATE TABLE orgtrack_core_profile_cache (
            scope_key TEXT PRIMARY KEY,
            fingerprint TEXT NOT NULL,
            payload_json TEXT NOT NULL,
            computed_at TEXT NOT NULL
        );
CREATE TABLE agent_inbox_delivery_resolutions (
            inbox_id INTEGER PRIMARY KEY,
            org_run_id TEXT NOT NULL,
            resolution_kind TEXT NOT NULL
                CHECK(resolution_kind IN ('cancelled', 'superseded')),
            resolved_by_member_id TEXT NOT NULL,
            reason TEXT NOT NULL,
            replacement_inbox_id INTEGER,
            replacement_task_id TEXT,
            created_at TEXT NOT NULL,
            CHECK(
                (resolution_kind='cancelled'
                    AND replacement_inbox_id IS NULL
                    AND replacement_task_id IS NULL)
                OR
                (resolution_kind='superseded'
                    AND ((replacement_inbox_id IS NOT NULL)
                         <> (replacement_task_id IS NOT NULL)))
            )
        );
CREATE INDEX idx_agent_inbox_delivery_resolutions_run
            ON agent_inbox_delivery_resolutions(org_run_id, inbox_id);
CREATE TABLE agent_org_task_run_schema_migrations (
            name TEXT NOT NULL,
            org_run_id TEXT NOT NULL,
            applied_at TEXT NOT NULL,
            PRIMARY KEY (name, org_run_id)
        );
CREATE INDEX idx_learnings_active
            ON learnings(agent_scope, status)
            WHERE status NOT IN ('deprecated', 'abandoned');
