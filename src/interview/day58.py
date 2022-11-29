def jumpToEnd(nums, idx=0):
    step = 0
    min = len(nums)
    if idx >= len(nums)-1:
        return min
    for i in range(nums[idx]):
        step = 1 + jumpToEnd(nums, idx+i+1)
        min = step if step < min else min

print(jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4]))
# 2