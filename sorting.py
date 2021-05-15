#
# Insertion Sorting 
#
# @param 
# A - Array
#
# @return
# A - Sorting Array
#
def insertion_sort(A):

    for j in range(1,len(A)):  
        key = A[j]
        i = j - 1

        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        
        A[i+1] = key
    
    return A

#
# Merge Sorting 
#
# @param 
# A - Array
# p - Array Start
# r - Array End
#
# @return
# A - Sorting Array
#
def merge_sort(A, p, r):
    # p <= q < r
    q = (p+r) // 2

    if(p == r):
        return
    
    merge_sort(A, p, q)
    merge_sort(A, q+1, r)

    return _merge(A, p, q, r)


def _merge(A, p, q, r):
    #Output Array 
    B = []

    i = p
    j = q+1

    while True:
        if(A[i] <= A[j]):
            B.append(A[i])
            
            if(i == q):
                B.extend(A[j:r+1]) #Inserir a segunda pilha em B
                break

            i += 1
        else:
            B.append(A[j])

            if(j == r):
                B.extend(A[i:q+1]) #Inserir a primeira pilha em B
                break

            j += 1
    
    A[p:r+1] = B

    return A

