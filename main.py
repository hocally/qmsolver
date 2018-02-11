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


def removeduplicates(values):
	output = []
	seen = set()
	for value in values:
		if value not in seen:
			output.append(value)
			seen.add(value)
	return output


def removedashes(L):
	N = []
	for A in L:
		for B in L:
			if hamming(A, B) > 1:
				N.append(B)
	return L


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


def comparegroups(L, M):
	print(L)
	print(M)
	N = []
	for i in range(0, len(L) - 1):
		for j in range(0, len(M) - 1):
			if hamming(L[i], M[j]) == 1:
				N.append(compareterms(L[i], M[j]))
				L.pop(i)
				M.pop(j)
			else:
				N.append(L[i])
				N.append(M[j])
	return N


def runalgorithim(L):
	c = 0
	N = []
	for c in range(0, len(L) - 1):
		N.extend(comparegroups(L[c], L[c + 1]))
		c += 1
	return N


L = mintermgen([0, 1, 2, 3])
print(L)
L = sortbyones(L)
print(L)
L = groupbyones(L)
print(L)
L = runalgorithim(L)
print(L)
