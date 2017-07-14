# Sort binary array in linear time
# input: [1, 0, 1, 0, 1, 0, 0, 1]
# output: [0, 0, 0, 0, 1, 1, 1, 1]


def linear_solution(binary_array):
    zeros = 0
    for i in binary_array:
        if i == 0:
            zeros += 1
    for i in range(zeros):
        binary_array[i] = 0
    for i in range(zeros+1, len(binary_array)):
        binary_array[i] = 1
    return binary_array


print(linear_solution([1, 1, 1, 1, 1, 1, 0, 0, 0, 0]))
