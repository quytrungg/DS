def sortNums(nums):
  for idx, num in enumerate(nums):
     idx1 = 0
     idx3 = len(nums) - 1
     idx = 0
     
     while idx <= idx3:
         if nums[idx] == 1:
             nums[idx], nums[idx1] = nums[idx1], nums[idx]
             idx += 1
             idx1 += 1
         if nums[idx] == 2:
             idx += 1
         if nums[idx] == 3:
             nums[idx], nums[idx3] = nums[idx3], nums[idx]
             idx3 -= 1
     return nums
            
      
print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]