def find_min_max(nums):
    if nums == []:
        return -1
    max = min = nums[0]
    compare = 0
    for i in nums:
        if i > max:
            max = i
        elif i < min:
            min = i
        compare += 1
    print(compare)
    return min, max

print(find_min_max([3, 5, 1, 2, 4, 8]))
# (1, 8)