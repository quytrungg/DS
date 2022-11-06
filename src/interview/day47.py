class Solution:
  def intersection(self, nums1, nums2):
    if len(nums2) > len(nums1):
        return self.intersection(nums2, nums1)
    result = []
    for i in range(len(nums2)-1):
        if nums2[i] in nums1:
            begin = i
            for j in range(i+1, len(nums2)):
                if nums2[j] == nums1[nums1.index(nums2[begin]) + (j-begin)]:
                    result.append(nums2[j])
            result.append(nums2[i])
            if len(result) == len(nums2):
                break
    return result


print(Solution().intersection([4, 9, 5], [9, 4, 9, 5, 8, 4]))
# [9, 4]