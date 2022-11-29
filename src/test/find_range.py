def findRanges(nums):
    if len(nums) == 0:
        return []
    elif len(nums) == 1:
        return f'{nums[0]} -> {nums[0]}'
    else:
        st = 0
        end = 0
        KQ = []
        for i in range(1, len(nums)):
            if(nums[i-1] != nums[i] - 1):
                if (nums[i - 1] != nums[i]):
                    temp = f'{st} "->" {end}'
                    KQ.append(temp)
                    st = nums[i]
            end = nums[i]

        temp = f'{st} "->" {end}'
        KQ.append(temp)
    return KQ


print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0->2', '5->5', '7->11', '15->15']
