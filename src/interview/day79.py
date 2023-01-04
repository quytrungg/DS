class Solution():
  def plusOne(self, digits):
    temp = 1
    digits = digits[::-1]
    for i in range(len(digits)):
        if (digits[i] + temp) == 10:
            digits[i] = 0
        else:
            digits[i] += temp
            temp = 0
    return digits[::-1]

num = [2, 9, 9]
print(Solution().plusOne(num))
# [3, 0, 0]