#! /usr/bin/python

class MapBase(MutableMapping):
	"""docstring for MapBase"""


	class _Item:
		"""docstring for _Item"""

		__slots__ = 

		def __init__(self, arg):
			super(_Item, self).__init__()
			self.arg = arg
			



	def __init__(self, arg):
		super(MapBase, self).__init__()
		self.arg = arg
		