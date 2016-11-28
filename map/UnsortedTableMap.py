#! /usr/bin/python

import MapBase

class UnsortedTableMap(MapBase):
	"""docstring for UnsortedTableMap"""
	def __init__(self):
		self._table = []

	def __getitem__(self, k):
		for item in self.table:
			if k == item._key:
				return item._value
		raise KeyError('Key Error:'+ repr(k))

	def __setitem__(self, k, v):
		for item in self.table:
			if k == item._key:
				item._value = v
				return
		self._table.append(self.Item(k, v))


	def __delitem__(self, k):
		for j in xrange(len(self._table):
			if k == self._table[k]._key:
				self._table.pop()
				return
		raise KeyError('Key Error: '+ repr(k))
		

	def __len__(self):
		return len(self._table)

	def __iter__(self):
		for item in self._table:
			yield item.key

