CREATE TABLE metadata (
               key TEXT PRIMARY KEY,
               value TEXT NOT NULL
             );
CREATE TABLE files (
               path TEXT PRIMARY KEY,
               content_hash TEXT NOT NULL,
               language TEXT NOT NULL,
               size INTEGER NOT NULL,
               modified_at INTEGER NOT NULL,
               indexed_at INTEGER NOT NULL,
               node_count INTEGER NOT NULL DEFAULT 0,
               errors_json TEXT NOT NULL DEFAULT '[]',
               stale INTEGER NOT NULL DEFAULT 0
             );
CREATE TABLE nodes (
               id TEXT PRIMARY KEY,
               kind TEXT NOT NULL,
               name TEXT NOT NULL,
               qualified_name TEXT NOT NULL,
               file_path TEXT NOT NULL,
               language TEXT NOT NULL,
               start_line INTEGER NOT NULL,
               end_line INTEGER NOT NULL,
               start_column INTEGER NOT NULL,
               end_column INTEGER NOT NULL,
               signature TEXT,
               updated_at INTEGER NOT NULL,
               confidence TEXT NOT NULL DEFAULT 'heuristic',
               extraction_method TEXT NOT NULL DEFAULT 'regex',
               parent_id TEXT,
               FOREIGN KEY(file_path) REFERENCES files(path) ON DELETE CASCADE,
               FOREIGN KEY(parent_id) REFERENCES nodes(id) ON DELETE SET NULL
             );
CREATE INDEX idx_nodes_name ON nodes(name);
CREATE INDEX idx_nodes_qualified_name ON nodes(qualified_name);
CREATE INDEX idx_nodes_file_path ON nodes(file_path);
CREATE INDEX idx_nodes_kind ON nodes(kind);
CREATE INDEX idx_nodes_language ON nodes(language);
CREATE TABLE edges (
               source TEXT NOT NULL,
               target TEXT NOT NULL,
               kind TEXT NOT NULL,
               line INTEGER,
               column INTEGER,
               provenance TEXT,
               confidence TEXT NOT NULL DEFAULT 'heuristic',
               resolution_status TEXT NOT NULL DEFAULT 'resolved',
               PRIMARY KEY(source, target, kind, line, column),
               FOREIGN KEY(source) REFERENCES nodes(id) ON DELETE CASCADE,
               FOREIGN KEY(target) REFERENCES nodes(id) ON DELETE CASCADE
             );
CREATE INDEX idx_edges_source ON edges(source);
CREATE INDEX idx_edges_target ON edges(target);
CREATE INDEX idx_edges_kind ON edges(kind);
CREATE TABLE unresolved_refs (
               file_path TEXT NOT NULL,
               from_node_id TEXT,
               name TEXT NOT NULL,
               kind TEXT NOT NULL,
               language TEXT NOT NULL DEFAULT 'typescript',
               line INTEGER NOT NULL,
               column INTEGER NOT NULL,
               candidates_json TEXT NOT NULL DEFAULT '[]',
               reason TEXT,
               FOREIGN KEY(file_path) REFERENCES files(path) ON DELETE CASCADE,
               FOREIGN KEY(from_node_id) REFERENCES nodes(id) ON DELETE SET NULL
             );
CREATE INDEX idx_unresolved_refs_file_path ON unresolved_refs(file_path);
CREATE INDEX idx_unresolved_refs_name ON unresolved_refs(name);
CREATE VIRTUAL TABLE nodes_fts USING fts5(
  id UNINDEXED,
  name,
  qualified_name,
  file_path,
  signature,
  content=''
)
/* nodes_fts(id,name,qualified_name,file_path,signature) */;
CREATE TABLE IF NOT EXISTS 'nodes_fts_data'(id INTEGER PRIMARY KEY, block BLOB);
CREATE TABLE IF NOT EXISTS 'nodes_fts_idx'(segid, term, pgno, PRIMARY KEY(segid, term)) WITHOUT ROWID;
CREATE TABLE IF NOT EXISTS 'nodes_fts_docsize'(id INTEGER PRIMARY KEY, sz BLOB);
CREATE TABLE IF NOT EXISTS 'nodes_fts_config'(k PRIMARY KEY, v) WITHOUT ROWID;
