def insertion_sort(A):
    if A is None:
        return
    for i in range(1, len(A)):
        current_value = A[i]
        position = i
        while position > 0 and A[position-1] > current_value:
            A[position] = A[position-1]
            position -= 1
        A[position] = current_value
    return A


print(insertion_sort([4, 3, 9, 10, 4, 1, 5]))
