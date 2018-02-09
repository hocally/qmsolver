def ones(N):
	o = 0
	for B in N:
		if B == '1':
			o += 1
	return o


def hamming(A, B):
	d = 0
	c = 0
	if len(A) != len(B):
		return None
	while c < len(A):
		if A[c] != B[c]:
			d += 1
		c += 1
	return d


def mintermgen(L):
	m = []
	for N in L:
		m += [format(N, '08b')]
	return m


def sortbyones(L):
	c = 0
	s = True
	while True:
		s = True
		c = 0
		while c < len(L) - 1:
			if ones(L[c]) > ones(L[c + 1]):
				s = False
				t = L[c + 1]
				L[c + 1] = L[c]
				L[c] = t
			c += 1
		if s:
			break
	return L


def groupbyones(L):
	R = []
	T = L
	while len(T) > 1:
		c = 0
		o = onesrow(T[0], ones(T[0]))
		while c < o:
			S = []
			S.append(T[c])
			R.append(S)
			c += 1
		T = T[c:]
	return T


def onesrow(L, O):
	c = 0
	for N in L:
		if ones(N) == O:
			c += 1
		else:
			break
	return c


l = mintermgen([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(l)
l = sortbyones(l)
print(l)
l = groupbyones(l)
print(l)
