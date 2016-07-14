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