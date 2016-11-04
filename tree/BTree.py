#! /usr/bin/python

import Node as nd

class BTree:
	"b tree"

	root = None

	def __init__(self, node):
		self.root = node

	def add(self, key, name):
		print '!***add node to the tree***!'
		print 'key is %d' % key
		print 'name is ', name
		node = nd.Node(key, name, None, None)	
		

	def displayPre(self, node):
		print '!***display nodes of the tree***!'
		print 'key is %d' % node.key
		print 'name is ', node.name
		if node.left:
			self.display(node.left)
		if node.right:
			self.display(node.right)

if __name__ == '__main__':
	
	l1_left = nd.Node(5, 'tom', None, None)
	l2_right = nd.Node(8, 'lily', None, None)
	root = nd.Node(1, 'henry', l1_left, l2_right)
	
	bt = BTree(root)
	bt.display(root)


