alp = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'O', 'R', 'S', \
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

class Solution:
  def convertToTitle(self, n):
    result = ''
    while n / 26 > 1:
        result += 'A'
        n /= 26
    return result + alp[n]

input1 = 1
input2 = 456976
input3 = 28
print(Solution().convertToTitle(input1))
# A
print(Solution().convertToTitle(input2))
# YYYZ
print(Solution().convertToTitle(input3))
# AB