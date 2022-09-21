def findPythagoreanTriplets(nums):
  sqr_arr = [i ** 2 for i in nums]
  for i in range(len(nums) - 1):
    for j in range(i+1, len(nums)):
        if nums[i] ** 2 + nums[j] ** 2 in sqr_arr:
            return True
  return False


print(findPythagoreanTriplets([3, 12, 5, 13]))
# True