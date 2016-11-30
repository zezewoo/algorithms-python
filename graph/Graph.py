#! /usr/bin/python



class Vertex:
	"""docstring for Vertex"""

	__slot__ = '_element'


	def __init__(self, x):
		self._element = x

	def element(self):
		return self._element

	def __hash__(self):
		return hash(self._element)


class Edge:
	"""docstring for Edge"""
	
	__slot__ = '_origin', '_destination', '_element'

	def __init__(self, u, v, x):
		self._origin = u
		self._destination = v
		self._element = x


	def endpoints(self):
		return (self._origin, self._destination)

	def opposite(self, v):
		return self._destination if v is self._origin else self._origin

	def element(self):
		return self._element


class Graph:
	"""docstring for Graph"""

	def __init__(self, directed=False):
		self._outgoing = {}
		self._incoming = {} if directed else self._outgoing

	def is_directed(self):
		return self._incoming is not self._outgoing

	def vertex_count(self):
		return len(self._outgoing)

	def vertices(self):
		return self._outgoing.keys()

	def edge_count(self):
		total = sum(len(self._outgoing[v]) for v in self._outgoing)
		return total if self.is_directed() else total//2

	def edges(self):
		result = set()
		for secondary_map in self._outgoing.values():
			result.update(secondary_map.values())
		return result


	def get_edges(self,u,v):
		return self._outgoing[u].get(v)

	def degree(self, v, outgoing=True):
		adj = self._outgoing if outgoing else self._incoming
		return len(adj[v])

	def incident_edges(self, v, outgoing=True):
		adj = self._outgoing if outgoing else self._incoming
		for edge in adj[v].values():
			yield edge

	def insert_vertex(self, x=None):
		v = self.Vertex(x)
		self._outgoing[v] = {}
		if self.is_directed():
			self._incoming[v] = {}
		return v

	def insert_edge(self, u, v, x=None):
		e = self.Edge(u,v,x)
		self._outgoing[u][v] = e
		self._incoming[v][u] = e


	def DFS(g, u, discovered):
		for e in g.incident_edges(u):
			v = e.opposite(u)
			if v not in discovered:
				discovered[v] = e
				DFS(g, v, discovered)


	def construct_path(u, v, discovered):
		path = []
		for v in discovered:
			path.append(v)
			walk = v
			while walk is not u:
				e = discovered[walk]
				parent = e.opposite(walk)
				path.append(parent)
				parent = walk
			path.reverse()
		return path


	def DFS_complete(g):
		forest = {}
		for u in g.vertices():
			if u not in forest:
				forest[u] = None
				DFS(g, u, forest)
		return forest



	def BFS(g, s, discovered):
		level = [s]
		while len(level) > 0:
			next_level = []
			for u in level:
				for e in g.incident_edges(u):
					v = e.opposite(u)
					if v not in discovered:
						discovered[v] = e
						next_level.append(v)
			next_level = level		








