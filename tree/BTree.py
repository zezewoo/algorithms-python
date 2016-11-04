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
		if self.root == None:
			self.root = node
			return

		current = self.root
		while current:
			print 'trace ..'
			if current.key > key and current.left != None:
				print 'trace left'
				current = current.left
			elif current.key < key and current.right != None:
				print 'trace right'
				current = current.right
			else :
				break
		current.left, node.left = node, current.left
		
	def displayPre(self, node):
		print '!***display nodes of the tree***!'
		print 'key is %d' % node.key
		print 'name is ', node.name
		if node.left:
			self.displayPre(node.left)
		if node.right:
			self.displayPre(node.right)

if __name__ == '__main__':
	
	l1_left = nd.Node(5, 'tom', None, None)
	l2_right = nd.Node(18, 'lily', None, None)
	root = nd.Node(10, 'henry', l1_left, l2_right)
	
	bt = BTree(root)
	# bt.displayPre(root)

	bt.add(4, 'jack')
	bt.displayPre(root)

