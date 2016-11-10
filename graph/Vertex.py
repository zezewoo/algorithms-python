#! /usr/bin/python

class Vertex:
	"""docstring for Vertex"""

	__slot__ = '_element'

	def __init__(self, x):
		self._element = x

	def element(self):
		return self._element

	def __hash__():
		return hash(id(self))

		