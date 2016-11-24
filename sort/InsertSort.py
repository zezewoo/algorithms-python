#! /usr/bin/python

def insert_sort(A):
	
	for x in xrange(1,len(A)):
		i = x
		cur = A[x]
		while i > 0 and A[i-1] > cur:
			A[i] = A[i-1]
			i -= 1
		A[i] = cur
	return A

if __name__ == '__main__':
	
	A = [122,33,4444,2,112,33334,12,53,3,22]
	print insert_sort(A)