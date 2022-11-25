roman = {
    'I':     1,
    'IV':    4,
    'V':     5,
    'IX':    9, 
    'X':     10,
    'XL':    40,
    'L':     50,
    'XC':    90,
    'C':     100,
    'CD':    400,
    'D':     500,
    'CM':    900,
    'M':     1000
}

class Solution():
  def romanToInt(self, s):
    num = 0
    for i in s:
        num += roman[i]
    return num
    
n = 'MCMX'
print(Solution().romanToInt(n))
# 1910