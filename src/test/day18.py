class Solution:
    def moveZeros(self, nums):
        nonZeroPos = 0
        
        for i in nums:
            if i != 0:
                nums[nonZeroPos] = i
                nonZeroPos += 1
           
        for i in range(len(nums) - nonZeroPos):
            nums[nonZeroPos + i] = 0

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]