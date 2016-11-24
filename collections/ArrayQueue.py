#! /usr/bin/python

class ArrayQueue:
	"""docstring for ArrayQueue"""

	DEFAULT_CAPACITY = 10

	def __init__(self):
		self._data = [None] *  ArrayQueue.DEFAULT_CAPACITY
		self._size = 0
		self._front = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def first(self):
		if self.is empty():
			raise Empty('Queue is empty')
		return self._data[self._front]

	def dequeue(self):
		if self.is empty():
			raise Empty('Queue is empty')
		answer = self._data[self._front]
		self._data[self._front] = None
		self._front = (self._front + 1) % len(self._data)
		self._size -= 1
		return answer

	def enqueue(self, e):
		if self._size == len(self._data):
			self._resize(2*len(self.data))
		avail = (self._front + self._size) % len(self._data)
		self[avail] = e
		self._size += 1

	def _resize(self,c):
		old = self._data
		self._data = [None] * c
		walk = self._front
		for x in xrange(self._size):
			self._data[x] = old[walk]
			walk = (walk + 1) % len(old)
		self._front = 0

	





		