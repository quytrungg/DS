class Solution(object):
  def findSingle(self, nums):
    count = {}
    for i in nums:
        try:
            count[i] += 1
        except:
            count[i] = 1
    for i, j in count.items():
        if j == 1:
            return i
    return None

nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print(Solution().findSingle(nums))
# 3