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
	S = []
	while len(L) > 0:
		c = 0
		o = onesrow(L, ones(L[0]))
		while c < o:
			S.append(L[c])
			c += 1
		R.append(S)
		S = []
		L = L[o:]
	return R


def onesrow(L, O):
	c = 0
	for N in L:
		if ones(N) == O:
			c += 1
		else:
			break
	return c


def compareterms(A, B):
	if len(A) != len(B):
		return None
	c = 0
	while c < len(A):
		if A[c] != B[c]:
			C = list(A)
			C[c] = '-'
			C = ''.join(C)
			return C
		c += 1
	return None


def comparegroups(L):
	T = L
	N = []
	i = 0
	for i in range(0, len(L) - 2):
		for j in range(i + 1, len(L) - 1):
			if hamming(L[i], L[j]) == 1:
				N.append(compareterms(L[i], L[j]))
				L[i].remove(L[i])
				L[j].remove(L[j])
			else:
				N.append(L[i])
				N.append(L[j])
			j += 1
		i += 1
	return N


l = mintermgen([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(l)
l = sortbyones(l)
print(l)
print(groupbyones(l))
print(comparegroups(groupbyones(l)))
