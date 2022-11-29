def findRanges(nums):
    begin = end = -1
    idx = 0
    result = []
    while idx < len(nums) - 1:
        begin = nums[idx]
        while nums[idx+1] - nums[idx] < 2:
            idx += 1
            if idx + 1 == len(nums):
                break
        end  = nums[idx]
        result.append(f'{begin}->{end}')
        idx += 1
        if idx == len(nums) - 1:
            result.append(f'{nums[idx]}->{nums[idx]}')
            break
    return result

print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0->2', '5->5', '7->11', '15->15']