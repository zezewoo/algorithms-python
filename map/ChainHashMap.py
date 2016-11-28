#! /usr/bin/python

class ChainHashMap(HashMapBase):
	"""docstring for ChainHashMap"""
	def _bucket_getitem(self, j, k):
		bucket = self._table[j]
		if bucket is None:
			raise KeyError('Key Error:'+ repr(k))
		return bucket[k]

	def _bucket_setitem(self, j, k, v):
		if self._table[j] is None:
			self._table[j] = UnsortedTableMap()
		oldsize = len(self._table[j])
		self._table[j][k] = v
		if len(self._table[j]) > oldsize:
			self._n += 1


	def _bucket_delitem(self, j, k):
		bucket = self._table[j]
		if bucket is None:
			raise KeyError('Key Error: '+ repr(k))
		del bucket[k]


	def __iter__(self):
		for bucket in self._table:
			if bucket is not None:
				for k in bucket:
					yield k

