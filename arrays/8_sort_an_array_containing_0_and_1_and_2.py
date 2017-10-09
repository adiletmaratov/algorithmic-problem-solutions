# Problem: http://www.techiedelight.com/sort-array-containing-0s-1s-2s-dutch-national-flag-problem/


def linear_solution(A):
    i, j, r, p = 0, 0, len(A) - 1, 1
    while r >= j:
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i, j = i + 1, j + 1
        elif A[j] > p:
            A[j], A[r] = A[r], A[j]
            r -= 1
        else:
            j += 1
    return A


#  stress test
import random

n = 100
for _ in range(1000):
    A = [random.randint(0, 2) for __ in range(n)]
    python_sort = sorted(A)
    linear = linear_solution(A)
    try:
        assert python_sort == linear
    except AssertionError:
        print(A)
        print(python_sort)
        print(linear)
        break
