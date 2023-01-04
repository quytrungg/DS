def sort_partially_sorted(nums, k):
    result = nums[:k]
    result = sorted(result)
    return result + nums[k:]

print(sort_partially_sorted([3, 2, 6, 5, 4], 2))
# [2, 3, 4, 5, 6]