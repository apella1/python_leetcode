def find_max_average(nums, k):
    num_sum = 0
    for i in range(k):
        num_sum += nums[i]
    max_sum = num_sum
    start_index = 0
    end_index = k
    while end_index < len(nums):
        num_sum -= nums[start_index]
        start_index += 1
        num_sum += nums[end_index]
        end_index += 1
        max_sum = max(max_sum, num_sum)

    return max_sum / k


print(find_max_average([1, 12, -5, -6, 50, 3], 4))
