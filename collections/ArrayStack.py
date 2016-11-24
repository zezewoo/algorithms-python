#! /usr/bin/python

class ArrayStack:
	"""docstring for ArrayStack"""
	def __init__(self,):
		self._data = []

	def __len__(self):
		return len(self._data)

	def is_empty(self):
		return len(self._data) == 0

	def push(self, value):
		return self._data.append(value)

	def top(self):
		if self.is empty():
    		raise Empty( Stack is empty )
		return self._data[-1]

	def pop(self):
		if self.is empty():
    		raise Empty( Stack is empty )
		return self._data.pop()

	