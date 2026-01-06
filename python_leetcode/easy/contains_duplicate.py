"""NeetCode 150: Arrays and Hashing"""


# time -> O(n^2)
# space -> O(1)
def contains_duplicate(nums: list[int]) -> bool:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


# bottleneck on storing the entire dictionary KV pairs and increments before checking for duplicates
# the contains_duplicate_hashmap_no_check() is more efficient than this
# the use of a hash set is more efficient as it only stores the keys
def contains_duplicate_hashmap(nums: list[int]) -> bool:
    nums_map = {}
    for num in nums:
        if num not in nums_map:
            # ! checking key in map
            nums_map[num] = 0
        nums_map[num] += 1
        if nums_map[num] > 1:
            return True
    return False


def contains_duplicate_hashmap_no_check(nums: list[int]) -> bool:
    nums_map = {}
    for num in nums:
        if num in nums_map.keys():
            return True
        nums_map[num] = 1
    return False


# time -> O(n)
# space -> O(n)
def contains_duplicate_hashset(nums: list[int]) -> bool:
    hash_set = set()
    for n in nums:
        if n in hash_set:
            return True
        hash_set.add(n)
    return False


# exhaustive operation - can trigger out of memory errors for large data sets
def contains_duplicate_pro(nums: list[int]) -> bool:
    return len(set(nums)) != len(nums)
