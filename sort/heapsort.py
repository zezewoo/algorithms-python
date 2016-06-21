def left(i):
	return i<<1

def right(i):
	return i<<1+1

def parent(i):
	return i>>1

def max_heapify(A, i):
	l = left(i)
	r = right(i)
	lagest = 0
	if l <= len(A) and A[l] > A[i]:
		lagest = l
	else:
		lagest = i
	
	if r <= len(A) and A[r] > A[lagest]:
		lagest = r
	if lagest != i:
		tmp = A[i]
		A[i] = A[lagest]
		A[lagest] = tmp
		max_heapify(A, lagest)
	
def build_max_heap(A):
	
	for i in range(len(A)/2, 1):
		max_heapify(A, i)
	return A
