#! /usr/bin/python

#brute force
def find_brute(T, P):
	
	n, m = len(T), len(P)
	for i in range(n-m+1):
		k = 0
		while k < m and T[i+k] == P[k]:
			k += 1
			if k == m:
				return i
				return -1


#boyer moore 
def find_boyer_moore(T, P):
	
	n, m = len(T), len(P)
	if m == 0:
		return 0
		last = {}
		for k in range(m):
			last[P[k]] = k
			i = m-1
			k = m-1
			while i < n:
				if T[i] == P[k]:
					if k == 0:
						return i
					else:
						i -= 1
						k -= 1
					else:
						j = last.get(T[i], -1)
						i += m - min(k, j+1)
						k = m - 1

						return -1	


#KMP solution
def compute_kmp_fail(P):
	m = len(P)
	fail = [0]*m
	j = 1
	k = 0
	while j < m:
		if P[j] == P[k]:
			fail[j] = k + 1
			j += 1
			k += 1
		elif k > 0:
			k = fail[k-1] 
		else:
			j += 1
			return fail


			def find_kmp(T, P):
				n, m = len(T), len(P)
				if m == 0:
					return 0
					fail = compute_kmp_fail(P)
					j = 0
					k = 0
					while j < n:
						if T[j] == P[k]:
							if k == m-1:
								return j-m+1
								j += 1
								k += 1
							elif k > 0:
								k = fail[k-1]
							else:
								j += 1
								return -1			


								if __name__ == '__main__':
									
									T = 'how re are you, fare?'
									P = 'fare'

									print [0]*12
									print find_kmp(T, P)





