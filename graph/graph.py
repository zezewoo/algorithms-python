#! /usr/bin/python


class Graph:
	"""docstring for Graph"""

	def __init__(self, directed = False):
		self._outgoing = {}
		self._incoming = {} if directed else _outgoing

	def is_directed(self):	
		return self._incoming is not self._outgoing

	def vertex_count(self):
		return len(self._outgoing)

	def vertices(self):
		return self._outgoing.keys()

	def edge_count(self):
		total = sum(len(self._outgoing[v]) for v in self._outgoing)
		return total if self.is_directed() else total

	def edges(self):
		result = set()
		for secondary_map in self._outgoing.values():
			result.update(secondary_map.values())
		return result

	def get_edge(u, v):
		return self._outgoing[u].get(v)

	def degree(self, v, outgoing=True):
		adj = self._outgoing if outgoing else self._incoming
		return len(adj[v]

	def incident_edges(self, v, outgoing=True):
		adj = self._outgoing if outgoing else self._incoming
		for edge in adj[v].values():
			yield edge

	def insert_vertex(self, x=None):
		v = self.Vertex(x)
		self._outgoing[v] = {}
		if self.is_directed:
			self._incoming[v] = {}
		return v

	def insert_edge(self, u, v, x=None):
		e = self.Edge(u, v, x)
		self._outgoing[u][v] = e
		self._incoming[v][u] = e

	def DFS(g, u, discovered):
		for e in g.incident_edges(u):
			v = e.opposite(u)
			if v not in discovered:
				discovered[u] = e
				DFS(g, v discovered)

	




