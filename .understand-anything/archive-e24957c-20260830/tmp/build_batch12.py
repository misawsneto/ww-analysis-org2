import json
import math
import sys

sys.path.insert(0, "/home/misael/pj/gui-repos/ORG2/.understand-anything/tmp")
import gen_batch12_data as g

ROOT = "/home/misael/pj/gui-repos/ORG2"

with open(f"{ROOT}/.understand-anything/tmp/ua-file-extract-results-12.json") as f:
    extract = json.load(f)
with open(f"{ROOT}/.understand-anything/intermediate/batch-inputs/batch-12.input.json") as f:
    inp = json.load(f)

batch_import_data = inp["batchImportData"]
results_by_path = {r["path"]: r for r in extract["results"]}

assert set(g.FILES.keys()) == set(r["path"] for r in extract["results"]), "FILES keys mismatch extraction results"

nodes = []
edges = []
node_ids = set()


def add_node(node):
    assert node["id"] not in node_ids, f"duplicate node id {node['id']}"
    node_ids.add(node["id"])
    nodes.append(node)


def add_edge(source, target, etype, weight):
    assert source != target, f"self-edge {source}"
    edges.append({"source": source, "target": target, "type": etype, "direction": "forward", "weight": weight})


def file_complexity(non_empty_lines):
    if non_empty_lines < 50:
        return "simple"
    if non_empty_lines <= 200:
        return "moderate"
    return "complex"


def func_complexity(start, end):
    n = end - start + 1
    if n < 15:
        return "simple"
    if n <= 60:
        return "moderate"
    return "complex"


def class_complexity(start, end, methods):
    n = end - start + 1
    if n < 20 and len(methods) < 3:
        return "simple"
    if n <= 80:
        return "moderate"
    return "complex"


# ---- File nodes ----
for path, (summary, tags, lang_notes) in g.FILES.items():
    r = results_by_path[path]
    node = {
        "id": f"file:{path}",
        "type": "file",
        "name": path.rsplit("/", 1)[-1],
        "filePath": path,
        "summary": summary,
        "tags": tags,
        "complexity": file_complexity(r["nonEmptyLines"]),
    }
    if lang_notes:
        node["languageNotes"] = lang_notes
    add_node(node)

# ---- Function nodes ----
func_line_lookup = {}
for path, funcs in g.FUNC.items():
    r = results_by_path[path]
    by_name = {fn["name"]: fn for fn in r["functions"]}
    for fname, (summary, tags) in funcs.items():
        fn = by_name.get(fname)
        assert fn is not None, f"function {fname} not found in extraction for {path}"
        func_line_lookup[(path, fname)] = (fn["startLine"], fn["endLine"])
        node = {
            "id": f"function:{path}:{fname}",
            "type": "function",
            "name": fname,
            "filePath": path,
            "lineRange": [fn["startLine"], fn["endLine"]],
            "summary": summary,
            "tags": tags,
            "complexity": func_complexity(fn["startLine"], fn["endLine"]),
        }
        add_node(node)

# ---- Class nodes ----
class_line_lookup = {}
for path, classes in g.CLASS.items():
    r = results_by_path[path]
    by_name = {c["name"]: c for c in r.get("classes", [])}
    for cname, (summary, tags) in classes.items():
        c = by_name.get(cname)
        assert c is not None, f"class {cname} not found in extraction for {path}"
        class_line_lookup[(path, cname)] = (c["startLine"], c["endLine"])
        node = {
            "id": f"class:{path}:{cname}",
            "type": "class",
            "name": cname,
            "filePath": path,
            "lineRange": [c["startLine"], c["endLine"]],
            "summary": summary,
            "tags": tags,
            "complexity": class_complexity(c["startLine"], c["endLine"], c.get("methods", [])),
        }
        add_node(node)

# ---- contains edges (file -> function/class) ----
for path, funcs in g.FUNC.items():
    for fname in funcs:
        add_edge(f"file:{path}", f"function:{path}:{fname}", "contains", 1.0)
for path, classes in g.CLASS.items():
    for cname in classes:
        add_edge(f"file:{path}", f"class:{path}:{cname}", "contains", 1.0)

# ---- exports edges (file -> function/class present in exports list) ----
for path in g.FILES:
    r = results_by_path[path]
    exported_names = {e["name"] for e in r.get("exports", [])}
    for fname in g.FUNC.get(path, {}):
        if fname in exported_names:
            add_edge(f"file:{path}", f"function:{path}:{fname}", "exports", 0.8)
    for cname in g.CLASS.get(path, {}):
        if cname in exported_names:
            add_edge(f"file:{path}", f"class:{path}:{cname}", "exports", 0.8)

# ---- imports edges (1:1 from batchImportData) ----
import_edge_count = 0
for path in g.FILES:
    targets = batch_import_data.get(path, [])
    for t in targets:
        add_edge(f"file:{path}", f"file:{t}", "imports", 0.7)
        import_edge_count += 1

expected_imports = sum(len(v) for v in batch_import_data.values())
assert import_edge_count == expected_imports, f"import edge count mismatch {import_edge_count} != {expected_imports}"

# ---- calls edges (same-batch) ----
for src_path, src_fn, dst_path, dst_fn in g.CROSS_CALLS:
    assert (src_path, src_fn) in func_line_lookup, f"missing caller {src_path}:{src_fn}"
    assert (dst_path, dst_fn) in func_line_lookup, f"missing callee {dst_path}:{dst_fn}"
    add_edge(f"function:{src_path}:{src_fn}", f"function:{dst_path}:{dst_fn}", "calls", 0.8)

# ---- calls edges (cross-batch, via neighborMap) ----
neighbor_map = inp.get("neighborMap", {})
for src_path, src_fn, dst_path, dst_fn in g.NEIGHBOR_CALLS:
    assert (src_path, src_fn) in func_line_lookup, f"missing caller {src_path}:{src_fn}"
    neighbors = neighbor_map.get(src_path, [])
    found = any(n["path"] == dst_path and dst_fn in n.get("symbols", []) for n in neighbors)
    assert found, f"neighbor {dst_path}:{dst_fn} not found for {src_path}"
    add_edge(f"function:{src_path}:{src_fn}", f"function:{dst_path}:{dst_fn}", "calls", 0.8)

print(f"nodes={len(nodes)} edges={len(edges)}")
print(f"import edges={import_edge_count} (expected {expected_imports})")

with open(f"{ROOT}/.understand-anything/tmp/batch12_nodes.json", "w") as f:
    json.dump(nodes, f)
with open(f"{ROOT}/.understand-anything/tmp/batch12_edges.json", "w") as f:
    json.dump(edges, f)

print("OK: assembled without assertion errors")
