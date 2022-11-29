def first_missing_positive(nums):
    missing = 1
    while missing in nums:
        missing += 1
    return missing

print(first_missing_positive([3, 4, -1, 1]))
# 2