import pickle, json, math, os

with open("/home/misael/pj/gui-repos/ORG2/.understand-anything/tmp/batch2_graph.pkl","rb") as fh:
    g = pickle.load(fh)
nodes = g["nodes"]
edges = g["edges"]

node_count = len(nodes)
edge_count = len(edges)
parts = max(1, math.ceil(max(node_count/60, edge_count/120)))
print("initial parts estimate:", parts)

# group nodes by filePath (file-level weight = own node + count of sub-nodes)
by_file = {}
for n in nodes:
    fp = n.get("filePath")
    by_file.setdefault(fp, []).append(n)

# edges are all sourced from a file: id (contains/exports/imports/tested_by/calls)
# map file path -> edges whose source belongs to that file
edges_by_file = {fp: [] for fp in by_file}
for e in edges:
    src = e["source"]
    assert src.startswith("file:")
    fp = src[len("file:"):]
    edges_by_file[fp].append(e)

# weight per file = nodes + edges (both matter for the 60/120 caps -> normalize edges/2 since cap ratio is 60:120=1:2)
def weight(fp):
    return len(by_file[fp]) + len(edges_by_file[fp]) / 2.0

files_sorted = sorted(by_file.keys(), key=lambda fp: -weight(fp))

# try increasing parts until greedy bin-packing respects caps
def try_pack(k):
    bins = [{"node":0,"edge":0,"files":[]} for _ in range(k)]
    for fp in files_sorted:
        nlen = len(by_file[fp]); elen = len(edges_by_file[fp])
        # pick bin with smallest current (node/60 + edge/120) load
        best = min(range(k), key=lambda i: bins[i]["node"]/60.0 + bins[i]["edge"]/120.0)
        bins[best]["node"] += nlen
        bins[best]["edge"] += elen
        bins[best]["files"].append(fp)
    ok = all(b["node"] <= 60 and b["edge"] <= 120 for b in bins)
    return ok, bins

k = parts
while True:
    ok, bins = try_pack(k)
    if ok:
        break
    k += 1
print("final parts:", k)
for i,b in enumerate(bins,1):
    print(f"part {i}: nodes={b['node']} edges={b['edge']} files={len(b['files'])}")

OUTDIR = "/home/misael/pj/gui-repos/ORG2/.understand-anything/intermediate"
total_n = 0
total_e = 0
if k == 1:
    outpath = f"{OUTDIR}/batch-2.json"
    with open(outpath,"w") as fh:
        all_nodes=[]; all_edges=[]
        for fp in bins[0]["files"]:
            all_nodes.extend(by_file[fp]); all_edges.extend(edges_by_file[fp])
        json.dump({"nodes": all_nodes, "edges": all_edges}, fh, indent=2)
        total_n += len(all_nodes); total_e += len(all_edges)
    print("WROTE", outpath, total_n, total_e)
else:
    for i,b in enumerate(bins,1):
        outpath = f"{OUTDIR}/batch-2-part-{i}.json"
        part_nodes=[]; part_edges=[]
        for fp in b["files"]:
            part_nodes.extend(by_file[fp]); part_edges.extend(edges_by_file[fp])
        with open(outpath,"w") as fh:
            json.dump({"nodes": part_nodes, "edges": part_edges}, fh, indent=2)
        total_n += len(part_nodes); total_e += len(part_edges)
        print("WROTE", outpath, len(part_nodes), len(part_edges))

print("GRAND TOTAL:", total_n, total_e, "expected", node_count, edge_count)
assert total_n == node_count
assert total_e == edge_count
