# !/usr/bin/python

def bubbleSort( input ):
	print 'start bubble sort'
	for i in range(len(input)-1, 0, -1):
		print i	
		for j in range(0, i):
				print j
				if input[j] > input[j+1]:
					input[j], input[j+1] = input[j+1], input[j]
	print input
	return input

