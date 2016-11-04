#! /usr/bin/python


class Node():
	
	#node of a tree
	key = 0
	name = ''
	left = None
	right = None

	def __init__(self, vkey, vname, vleft, vright):
		self.key = vkey
		self.name = vname
		self.left = vleft
		self.right = vright
		