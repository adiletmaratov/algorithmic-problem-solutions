# Problem: http://www.techiedelight.com/find-maximum-length-sub-array-equal-number-0s-1s/


def linear_solution(A):
    results = [0, 0]
    sum_counter = 0
    A = [1 if x else -1 for x in A]
    sums = {0: -1}
    for counter, value in enumerate(A):
        sum_counter += value
        if sum_counter not in sums:
            sums[sum_counter] = counter
        else:
            if results[1]-results[0] < counter - sums[sum_counter]:
                results[0] = sums[sum_counter]+1
                results[1] = counter+1
    return [1 if x > 0 else 0 for x in A[results[0]:results[1]]]


def naive_solution(A):
    l, r = 0, -1
    for i in range(len(A)):
        zc = 0
        oc = 0
        for j in range(i, len(A)):
            if A[j] == 1:
                oc += 1
            else:
                zc += 1
            if oc == zc and j - i > r - l:
                l, r = i, j
    return A[l:r+1]


# print(linear_solution([0, 1, 0]))
import random
n = 100
for _ in range(1000):
    A = [random.randint(0, 1) for __ in range(n)]
    naive = naive_solution(A)
    linear = linear_solution(A)
    try:
        assert naive == linear
    except AssertionError:
        print(A)
        print(naive)
        print(linear)
        break
