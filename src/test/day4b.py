class Solution:
  def lengthOfLongestSubstring(self, s):
    if len(s) == 0:
        return 0
    
    substring = ""

    length = 1
    maxLength = 0
    
    for i in range(len(s)):
        if(s[i] not in substring):
            substring += s[i]
            length += 1
            if(length > maxLength):
                maxLength = length
        else:
           substring = ""
           i = i - length + 1
           length = 0
           
    return maxLength
            
            

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10