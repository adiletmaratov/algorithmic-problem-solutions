def linear_solution(A):
    results = [0, 0]
    sum_counter = 0
    A = [1 if x else -1 for x in A]
    sums = {}
    for counter, value in enumerate(A):
        sum_counter += value
        if not sums.get(sum_counter):
            sums[sum_counter] = counter
        else:
            if results[1]-results[0] < counter - sums[sum_counter]:
                results[0] = sums[sum_counter]
                results[1] = counter
    return [1 if x > 0 else 0 for x in A[results[0]:results[1]]]
