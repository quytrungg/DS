def singleNumber(nums): #find 1st non-duplicated number
    for idx, num in enumerate(nums):
        if num in nums[idx + 1:] or num in nums[:idx]:
            continue
        return num
    return -1

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1