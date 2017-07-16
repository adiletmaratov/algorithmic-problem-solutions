# http://www.techiedelight.com/find-largest-sub-array-formed-by-consecutive-integers/


def solution(arr):
    if len(arr) == 0:
        return []
    result = (0, 0)
    for i in range(len(arr)):
        biggest, smallest = arr[i], arr[i]
        sub_array = set()
        for j in range(i, len(arr)):
            if arr[j] in sub_array:
                break
            biggest = max(arr[j], biggest)
            smallest = min(arr[j], smallest)
            sub_array.add(arr[j])
            if biggest - smallest + 1 == len(sub_array) and (result[1] - result[0] < biggest - smallest):
                result = i, j
    return arr[result[0]:result[1]+1]


print(solution([2, 0, 2, 1, 4, 3, 1, 0]))
print(solution([1, 2, 3, 8, 5, 6, 7]))