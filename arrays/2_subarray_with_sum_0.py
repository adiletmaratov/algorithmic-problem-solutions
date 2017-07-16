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


def linear_time_solution(arr):
    result = []
    sum_counter = 0
    sums_dict = {}
    for i in range(len(arr)):
        sum_counter += arr[i]
        if sums_dict.get(sum_counter):
            for j in sums_dict[sum_counter]:
                result.append(arr[j+1:i+1])
            sums_dict[sum_counter].append(i)
        else:
            sums_dict[sum_counter] = [i]
    return result


print(linear_time_solution([3, 4, -7, 3, 1, 3, 1, -4, -2, -2]))
print(linear_time_solution([4, 2, -3, -1, 0, 4]))
