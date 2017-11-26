import random


def insertion_sort(A):
    if A is None:
        return
    for i in range(len(A)):
        value = A[i]
        position = i
        while position > 0 and A[position-1] > value:
            A[position] = A[position-1]
            position -= 1
        A[position] = value
    return A


for i in range(1000):
    A = [random.randint(0, 1000) for __ in range(100)]
    assert sorted(A) == insertion_sort(A)
