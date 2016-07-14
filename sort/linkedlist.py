#!/usr/bin/python


class LinkedList:
	"docstring for LinkedList"

	def __init__(self, value, prev, next):

		print "init list"
		super(LinkedList, self).__init__()
		self.value = value
		self.prev  = prev
		self.next  = next
