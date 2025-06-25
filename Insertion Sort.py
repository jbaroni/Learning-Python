def InsertionSort(A):
    n = len(A)
    if n <=1:
        return #If array has 0 or 1 elements, it is already sorted, so return the array.
    
    for j in range(1, n): # remember python begins iterations at 0.
        key = A[j]
        # insert A[j] into the sorted sequence A[1...j-1]
        i = j - 1
        while i >= 0 and key < A[i]:
            A[i+1]=A[i]
            i = i - 1
        A[i+1] = key
        print(A)

arr = [12,11,13,5,6]
InsertionSort(arr)
print(arr)

A = [31,41,59,26,41,58]
InsertionSort(A)

# Time complexity = O(N^2)
# Auxiliary Space O(1)

def InsertionSortDec(A):
    n = len(A)
    if n <=1:
        return #If array has 0 or 1 elements, it is already sorted, so return the array.
    
    for j in range(1, n): # remember python begins iterations at 0.
        key = A[j]
        # insert A[j] into the sorted sequence A[1...j-1]
        i = j - 1
        while i >= 0 and key > A[i]:
            A[i+1]=A[i]
            i = i - 1
        A[i+1] = key
        print(A)
    
InsertionSortDec(arr)