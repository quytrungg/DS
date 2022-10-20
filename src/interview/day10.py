#question: given an array and number s, return shortest length of subarray that sum equals to s

class Solution:
    def minSubArrayLen(self, nums, s):
        min = len(nums)
        for i in range(len(nums)):
            sum = 0
            begin = end = i
            while sum < s and end < len(nums):
                sum += nums[end]
                end += 1
            if sum == s and end - begin < min:
                min = end - begin
        return min

print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
# 2