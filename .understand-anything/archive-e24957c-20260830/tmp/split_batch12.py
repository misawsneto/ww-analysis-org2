import json
import math
import sys

ROOT = "/home/misael/pj/gui-repos/ORG2"

with open(f"{ROOT}/.understand-anything/tmp/batch12_nodes.json") as f:
    nodes = json.load(f)
with open(f"{ROOT}/.understand-anything/tmp/batch12_edges.json") as f:
    edges = json.load(f)

node_count = len(nodes)
edge_count = len(edges)
print(f"nodeCount={node_count} edgeCount={edge_count}")

if node_count <= 60 and edge_count <= 120:
    parts_needed = 1
else:
    parts_needed = math.ceil(max(node_count / 60, edge_count / 120))
print(f"parts_needed={parts_needed}")

sys.path.insert(0, f"{ROOT}/.understand-anything/tmp")
import gen_batch12_data as g

all_files = sorted(g.FILES.keys())

# per-file node count (all nodes whose filePath == this file)
nodes_by_file = {p: [] for p in all_files}
for n in nodes:
    nodes_by_file[n["filePath"]].append(n)

# per-file outgoing-edge count (edges whose source belongs to this file)
node_id_to_file = {n["id"]: n["filePath"] for n in nodes}
edges_by_file = {p: [] for p in all_files}
for e in edges:
    src_file = node_id_to_file[e["source"]]
    edges_by_file[src_file].append(e)

file_node_counts = {p: len(nodes_by_file[p]) for p in all_files}
file_edge_counts = {p: len(edges_by_file[p]) for p in all_files}

NODE_CAP = 60
EDGE_CAP = 120

# Greedy sequential bin-packing over alphabetically sorted files, respecting caps.
groups = []
cur = []
cur_nodes = 0
cur_edges = 0
for p in all_files:
    fn = file_node_counts[p]
    fe = file_edge_counts[p]
    if cur and (cur_nodes + fn > NODE_CAP or cur_edges + fe > EDGE_CAP):
        groups.append(cur)
        cur = []
        cur_nodes = 0
        cur_edges = 0
    cur.append(p)
    cur_nodes += fn
    cur_edges += fe
if cur:
    groups.append(cur)

parts = len(groups)
print(f"parts_actual={parts}")
for i, grp in enumerate(groups):
    gn = sum(file_node_counts[p] for p in grp)
    ge = sum(file_edge_counts[p] for p in grp)
    print(f"group {i+1}: files={len(grp)} nodes={gn} edges={ge}")

file_to_group = {}
for gi, fg in enumerate(groups):
    for path in fg:
        file_to_group[path] = gi

node_id_to_group = {n["id"]: file_to_group[n["filePath"]] for n in nodes}

part_nodes = [[] for _ in range(parts)]
for n in nodes:
    part_nodes[node_id_to_group[n["id"]]].append(n)

part_edges = [[] for _ in range(parts)]
for e in edges:
    part_edges[node_id_to_group[e["source"]]].append(e)

total_nodes_written = 0
total_edges_written = 0
for i in range(parts):
    frag = {"nodes": part_nodes[i], "edges": part_edges[i]}
    if parts == 1:
        outpath = f"{ROOT}/.understand-anything/intermediate/batch-12.json"
    else:
        outpath = f"{ROOT}/.understand-anything/intermediate/batch-12-part-{i+1}.json"
    with open(outpath, "w") as f:
        json.dump(frag, f, indent=1)
    print(f"part {i+1}: nodes={len(part_nodes[i])} edges={len(part_edges[i])} -> {outpath}")
    total_nodes_written += len(part_nodes[i])
    total_edges_written += len(part_edges[i])

assert total_nodes_written == node_count
assert total_edges_written == edge_count
print(f"TOTAL nodes={total_nodes_written} edges={total_edges_written}")
