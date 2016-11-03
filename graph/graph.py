def walk(G, s, S=set()):
	P, Q = dict(), set()
	P[s] = None
	Q.add(s)
	while Q:
		u = Q.pop()
		for v in G[u].difference(P, S):
			Q.add(v)
			P[v] = u
	return P


def some_graph():
	a, b, c, d, e, f, g, h = range(8)
	N = [
		[b, c, d, e, f],
		[c, e],
		[d],
		[e],
		[f],
		[c, g, h],
		[f, h],
		[f, g]
	]
	return N

G = some_graph()
for i in range(len(G)):
	G[i] = set(G[i])
print list(walk(G, 0))

def tr(G):
	GT = {}
	for u in G: GT[u] = set()
	for u in G:
		for v in G[u]:
			GT[v].add(u)
	return GT

def scc(G):
	GT = tr(G)
	sccs, seen = [], set()
	for u in dfs_topsort(G):
		if u in seen: continue
		C = walk(GT, u, seen)
		seen.update(C)
		sccs.append(C)
	return sccs

from string import ascii_lowercase
def parse_graph(s):
	G = {}
	for u, line in zip(ascii_lowercase, s.split("/")):
		G[u] = set(line)
	return G

G = parse_graph('bc/die/d/ah/f/g/eh/i/h')
print list(map(list, scc(G)))
