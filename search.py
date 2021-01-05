def linear(A, k):
    
    for i in range(0,len(A)):
        if k == A[i]:
            return i

    return -1