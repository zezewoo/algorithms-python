#! /usr/bin/python



class SortedTableMap(MapBase):
	"""docstring for SortedTableMap"""

	def _find_index(self, k, low, high):
		if high < low:
			return high + 1
		else:
			mid = (low+high)//2
			if k == self._table[mid]._key:
				return mid
			elif k < self._table[mid]._key:
				return _find_index(k, 0, mid-1)
			else :
				return _find_index(k, mid+1, high)

	def __init__(self):
		self._table = []


	def __len__(self):
		return len(self._table)


	def __getitem__(self, k):
		j = self._find_index(k, 0, len(self._table)-1)
		if j == len(self._table) or self._table[j]._value != k:
			raise KeyError('Key Error: '+ repr(k))
		return self._table[j]._value


	def __setitem__(self, k, v):
		j = self._find_index(k, 0, len(self._table)-1)
		if j < len(self._table) and self._table[j]._value == k:
			self._table[j]._value = v
		else:
			self._table.insert(j, self._Item(k,v))


	def __delitem__(self, k):
		j = self._find_index(k, 0, len(self._table)-1)
		if j == len(self._table) or self._table[j]._value != k:
			raise KeyError('Key Error: '+ repr(k))
		self._table.pop(j)


	def __iter__(self):
		for item in self._table:
			yield item._key


	def __reversed__(self):
		for item in reversed(self._table):
			yield item._key


	def find_min(self):
		if len(self._table) > 0:
			return (self._table[0]._key, self._table[0]._value)
		else:
			return None

	def find_max(self):
		if len(self._table) > 0:
			return (self._table[-1]._key, self._table[-1]._value)
		else:
			return None














