# Given an unsorted array of integers, find a pair with given sum in it.
# ex. arr = [8, 7, 2, 5, 3, 1]
# ex. sum = 10
# output indexes 0, 2. values 8, 2. (True or False)


def find_pair_n_squared(nums, sum):
    for i in range(len(nums)):
        for y in range(len(nums)):
            if nums[i] + nums[y] == sum:
                return [i, y]


def pair_exists_logarithmic(nums, sum):
    sorted_nums = sorted(nums)
    low = 0
    high = len(nums) - 1
    for i in range(len(nums)):
        if sorted_nums[low] + sorted_nums[high] < sum:
            low += 1
        elif sorted_nums[low] + sorted_nums[high] > sum:
            high -= 1
        elif sorted_nums[low] + sorted_nums[high] == sum:
            return low, high


def pair_exists_linear(nums, sum):
    nums_dict = {}
    for num in nums:
        if nums_dict.get(sum-num):
            return True
        else:
            nums_dict[num] = num
    return False
