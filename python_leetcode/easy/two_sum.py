""" * Arrays and Hashing """
from pprint import pprint


# O(n2) time complexity
def two_sum(nums, target):
    for a in range(len(nums)):
        for b in range(1, len(nums)):
            if nums[a] + nums[b] == target and a != b:
                return [a, b]


# runtime 17ms (beats 38.98% of users), memory 17.02 mb (beats 85.79%)
def two_sum2(nums: list[int], target: int):
    for index, value in enumerate(nums):
        difference = target - value
        if difference in nums[index:] and (nums.index(difference) != index):
            return [index, nums.index(difference)]


# runtime 57ms (92.24%), memory 17.60 (45.01%)
def two_sum_hash_map(nums: list[int], target: int):
    prev_map = {}
    for y, z in enumerate(nums):
        diff = target - z
        if diff in prev_map:
            return [prev_map[diff], y]
        prev_map[z] = y


pprint(two_sum2([1, 2, 3, 4, 5], 8))
