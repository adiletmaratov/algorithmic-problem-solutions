# http://www.techiedelight.com/find-maximum-length-sub-array-having-given-sum/


def naive_solution(arr, given_sum):
    result = []
    for i in range(len(arr)):
        sub_sum = 0
        for y in range(i, len(arr)):
            sub_sum += arr[y]
            if sub_sum == given_sum:
                result.append(arr[i:y+1])
    return result


def linear_time_solution(arr, num):
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


print(naive_solution([4, 2, 2, 1, 2, 3, 2], 8))
print(linear_time_solution([4, 2, 2, 1, 2, 3, 2], 8))
