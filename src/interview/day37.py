class Solution(object):
  def threeSum(self, nums):
    neg_arr = []
    result = []
    for i in nums:
        if i < 0:
            neg_arr.append(i)
            nums.remove(i)
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            temp = (nums[i] + nums[j]) * -1
            if temp in neg_arr:
                result.append([temp, nums[i], nums[j]])
                neg_arr.remove(temp)

    return result

# Test Program
nums = [1, -2, 1, 0, 5]
print(Solution().threeSum(nums))
# [[-2, 1, 1]]