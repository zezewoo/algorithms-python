#! /usr/bin/python

class TreeMap(LinkedBinaryTree, MapBase):
	"""docstring for TreeMap"""

	class Position(LinkedBinaryTree.Position):
		"""docstring for Position"""
		
		def key(self):
			return self.element()._key

		def value(self):
			return self.element()._value
	
	
	def _subtree_search(self, p, k):
		if k == p.key():
			return p
		elif k < p.key():
			if self.left(p) is not None:
				return self._subtree_search(self.left(p), k)
		else:
			if self.right(p) is not None:
				return self._subtree_search(self.right(p), k)
		return p


	def _subtree_first_position(self, p):
		walk = p
		while self.left(walk) is not None:
			walk = self.left(walk)
		return walk



	def _subtree_last_position(self, p):
		walk = p
		while self.right(walk) is not None:
			walk = self.right(walk)
		return walk
		

	def first(self):
		return self._subtree_first_position(self.root()) if len(self) > 0 else None

	def last(self):
		return self._subtree_last_position(self.root()) if len(self) > 0 else None


	def before(self, p):
		self._validate(p)
		if self.left(p):
			return self._subtree_last_position(self.left(p))
		else:
			walk = p
			above = self.parent(walk)
			while above is not None and walk == self.left(above):
				walk = above
				above = self.parent(walk)
			return above

	def find_position(self, k):
		if self.is_empty():
			return None
		else:
			p = self._subtree_search(self.root(),k)
			self._rebalance_access(p)
			return p

	def find_min(self):
		if self.is_empty():
			return None
		else:
			p = self.first()
			return (p.key(), p.value())

	def __getitem(self, k):
		if self.is_empty():
			raise KeyError('Key Error:  '+ repr(k))
		else:
			p = self._subtree_search(self.root(), k)
			self._rebalance_access(p)
			if k != p.key():
				raise KeyError('Key Error:  ' + repr(k))
			return p.value()


	def __setitem__(self, k, v):
		if self.is_empty():
			leaf = self._add_root(self._Item(k,v))
		else:
			p = self._subtree_search(self.root(),k)
			if p.key() == k:
				p.value() = v
				self._rebalance_access(p)
				return
			else:
				item = self._Item(k,v)
				if p.key() < k:
					leaf = self._add_right(p, item)
				else:
					leaf = self._add_left(p, item)
		self._rebalance_insert(leaf)


	def __iter__(self):
		p = self.first()
		while p is not None:
			yield p.key()
			p = self.after(p)



















