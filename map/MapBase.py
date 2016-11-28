#! /usr/bin/python

import MutableMapping

class MapBase(MutableMapping):
	"""docstring for MapBase"""


	class _Item:
		"""docstring for _Item"""

		__slots__ = '_key', '_value'

		def __init__(self, k, v):
			self._key = k
			self._value = v

		def __eq__(self, other):
			return self._key == self._value
			
		def __ne__(self, other):
			return not self == other

		def __lt__(self, other):
			return self._key < other._key

	
		