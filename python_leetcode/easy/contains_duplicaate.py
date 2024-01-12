"""NeetCode 150: Arrays and Hashing"""


def contains_duplicate(nums: list[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


def contains_duplicate_hashmap(nums: list[int]) -> bool:
    nums_map = {}
    for num in nums:
        if num not in nums_map:
            nums_map[num] = 0
        nums_map[num] += 1
        if nums_map[num] > 1:
            return True
    return False
