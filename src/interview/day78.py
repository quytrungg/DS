class Solution(object):
  def findDisappearedNumbers(self, nums):
    result = []
    minN = min(nums)
    maxN = max(nums)
    for i in range(minN+1, maxN):
        if i not in nums:
            result.append(i)
    return result

nums = [4, 6, 2, 6, 7, 2, 1]
print(Solution().findDisappearedNumbers(nums))
# [3, 5]