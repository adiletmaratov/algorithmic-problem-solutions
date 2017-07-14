# Find a duplicate element in a limited range array
# Given array of size n with elements between 1 to n-1 with one element
# repeating. Find it
#
# input: [1, 2, 3, 4, 4]
# output: 4


def dictionary_solution(arr):
    elements = {}
    for element in arr:
        if elements.get(element):
            return element
        else:
            elements[element] = 1


def sign_inverting_solution(arr):
    """best solution possible"""
    for i in range(len(arr)):
        if arr[arr[i]-1] < 0:
            return arr[i]
        arr[arr[i]-1] = arr[i] * (-1)


def xor_solution(arr):
    """just for a possibility, this algo takes 2n time"""
    xor = 0
    for i in arr:
        xor ^= i
    for i in range(1, len(arr)):
        xor ^= i
    return xor


print(xor_solution([1, 2, 3, 4, 4]))
