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
        if s == True:
            break
    return L
    
def sortbyones(L):
    if len(L) == 1:
        return None
    if ones(L[0]) == ones(L[1]):
        return [[L[0]] + sortbyones(L[1:])
    

l = mintermgen([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(l)
print(sortbyones(l))
