class Solution:
  def sortColors(self, nums):
    indexZeros = 0
    indexOnes = 0
    indexTwos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[indexZeros], nums[i] = nums[i], nums[indexZeros]
            indexZeros += 1
    for i in range(len(nums)):
        if nums[i] != 1:
            nums[indexOnes], nums[i] = nums[i], nums[indexOnes]
            indexOnes += 1
    for i in range(len(nums)):
        if nums[i] != 2:
            nums[indexTwos], nums[i] = nums[i], nums[indexTwos]
            indexTwos += 1
    

nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

Solution().sortColors(nums)
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]