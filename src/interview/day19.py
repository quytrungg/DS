def findKthLargest(nums, k):
    max = 0
    for i in nums:
        if i > max:
            max = i
    temp = [False for _ in range(max+1)]
    for i in nums:
        temp[i] = True
    for i in range(len(temp) - 1, -1, -1):
        if temp[i]:
            if k == 1:
                return i
            else: k -= 1

print(findKthLargest([3, 5, 2, 6, 7, 8, 4, 8], 3))