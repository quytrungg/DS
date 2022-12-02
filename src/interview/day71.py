def longest_consecutive(nums):
    max = 1
    for i in nums:
        count = 1
        while i+1 in nums:
            count += 1
            i += 1
        max = count if count > max else max
    return max

print(longest_consecutive([100, 4, 200, 1, 3, 2]))
# 4