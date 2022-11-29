result = []

def permute(nums, i):
    if i == len(nums):
        return result
    for j in range(i, len(nums)):
        nums[i], nums[j] = nums[j], nums[i]
        result.append(nums)
        permute(nums, i+1)
        nums[i], nums[j] = nums[j], nums[i]

print(permute([1, 2, 3], 0))
# [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]