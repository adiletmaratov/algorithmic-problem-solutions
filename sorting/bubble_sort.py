def bubble_sort(A):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                swapped = True
    return A


print(bubble_sort([2, 5, 6, 7, 8, 9, 1, 4]))
