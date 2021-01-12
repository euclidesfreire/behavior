import math 

def linear(A, k):
    
    for i in range(0,len(A)):
        if A[i] == k:
            return i

    return -1

def binary(A,K):
    L = 0
    R = len(A) - 1

    while L <= R:
        M = (L+R) // 2

        if K == A[M]:
            return M 

        if K < A[M]:
            R = M - 1
        else:
            L = M + 1

    return -1

def binary_recursive(A,L,R,K):
    
    if R >= L:

        M = (L+R) // 2 

        if K == A[M]:
            return M

        if K < A[M]:
            R = M - 1
        else:
            L = M + 1

        return binary_recursive(A,L,R,K)

    else:
        return -1

def jump(A,K):
    n = len(A)
    step = int(math.sqrt(n))
    i = step

    while i < len(A):
        if A[i] >= K:
            break

        i += step

    for z in range(i-step, i):
        if A[z] == K:
            return z
    
    return -1