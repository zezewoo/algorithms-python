#! /usr/bin/python


class LinkedStack:
	"""docstring for LinkedStack"""

	class _Node:
		"""docstring for Node"""
		__slot__ = '_element', '_next'

		def __init__(self, element, next):
			self._element = element
			self._next = next


	def __init__(self):
		self._head = None
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def push(self, e):
		self._head = self._Node(e, self._head)
		self._size += 1

	def top(self):
		if self.is empty():
			raise Empty('Stack is empty')	
		return self._head._element

	def pop(self):
		if self.is empty():
			raise Empty('Stack is empty')
		answer = self._head._element
		self._head = self._head._next
		self._size -= 1
		return answer

	












		