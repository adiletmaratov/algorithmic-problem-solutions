def selection_sort(A):
    if A is None or len(A) < 2:
        return
    for i in range(len(A)):
        min_i = i
        for j in range(i, len(A)):
            if A[min_i] >= A[j]:
                min_i = j
        A[i], A[min_i] = A[min_i], A[i]
    return A


print(selection_sort([4, 3, 9, 10, 4, 1, 5]))
