#! /usr/bin/python
import ctypes


class DynamicArray:
	"""docstring for DynamicArray"""
	def __init__(self):
		self._n = 0
		self._capacity = 1
		self._A = self._make_array(self._capacity)
		
	def __len__(self):
		return self._n

	def __getitem__(self, k):
		if not 0 <= k < self._n:
			raise IndexError('invalid index')
		return self._A[k]

	def append(self, obj):
		if self._n == self._capacity:
			self._resize(2*self._capacity)
		self._A[n] = obj
		self._n += 1

	def insert(self, k, value):
		if self._n == self._capacity:
			self._resize(2*self._capacity)
		for j in range(self._n, k, -1):
			self._A[j] = self._A[j-1]
		self._A[k] = value
		self._n += 1

	def remove(self, k):
		if not 0 <= k < self._n:
			raise IndexError('invalid index')
		for j in range(self._n, k, -1):
			self._A[j] = self._A[j-1]
		self._n -= 1

	def _resize(self, c):
		B = self._make_array(c)
		for x in range(self._n):
			B[x] = self._A[x]
			self._A = B
			self._capacity = c

	def _make_array(self, c):
		return (c * ctypes.py_object)()

	def to_string(self):
		string = []
		for x in xrange(self._n):
			string.append(self._A[x])

if __name__ == '__main__':

	A = DynamicArray()
	A.insert(0, 'a')
	A.insert(1, 'b')


	print A.to_string()

	print 'hello DynamicArray'
