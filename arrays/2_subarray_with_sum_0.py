# Print all subarrays with sum 0
# example:
#   [4, 2, -3, -1, 0, 4]
#
# subarrays [-3, -1, 0, 4] and [0]

from collections import defaultdict

multimap = defaultdict(list)


def naive_solution(arr):
    result = []
    for i in range(len(arr)):
        sub_sum = 0
        for y in range(i, len(arr)):
            sub_sum += arr[y]
            if sub_sum == 0:
                result.append(arr[i:y+1])
    return result


print(naive_solution([3, 4, -7, 3, 1, 3, 1, -4, 2, 2]))
