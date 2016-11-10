#! /usr/bin/python


BLACK = 0  
RED = 1  
#graphic elements of rbtree for printing  
VC = '|'  
HC = '-'  
SIZE = 3  
RIG = '|-' + HC * SIZE  
LEF = '|-' + HC * SIZE  
SP = chr(32)  
IND1 = SP * (SIZE + 1)  
IND2 = VC + SP * SIZE  


class RBTreeNode:
	"""docstring for RBTreeNode"""
	def __init__(self, key = None, value = None, color = BLACK):
		self.key = key
		self.value = value 
		self.left = None
		self.right = None
		self.parent = None
		self.color = color


class RBTree:
	def __init__(self):
		self.nil = RBTreeNode()
		self.root = self.nil

	def __repr__(self):
		return '\n'

	def graph(self, x = False, prefix = ''):
		if x is False:
			x = self.root
		if x is not self.nil:
			parent = x.parent
			last_prefix = ''
			if parent is not self.nil:
				pp = parent.parent
				last_prefix = LEF if parent.left is x else RIG
				if pp is not self.nil:
					if pp.left is parent and parent.left is x:
						prefix += IND1
					else:
						prefix += IND2
			self.graph(x.right, prefix)
			print '%s%s%s' % (prefix, last_prefix, x)
			self.graph(x.left, prefix)
			return 

	def search(self, key, x=False):
		if x is False:
			x  = self.root
		while (x is not self.nil) and (key != x.key):
			if key < x.key:
				x = x.left
			else:
				x = x.right
		return x

	def insert(self, T, z):

		z.left = T.nil
		z.right = T.nil
		z.parent = T.nil

		y = T.nil
		x = T.root
		while x != T.nil:
			y = x
			if z.key < x.key:
				x = x.left
			else:
				x = x.right
		z.parent = y

if __name__ == '__main__':

	trd={'a':7,'b':1,'c':8,'d':2,'e':3}  
    tr=RBTree(trd.items())  
    print("after build from dict:")  
    print(tr)











