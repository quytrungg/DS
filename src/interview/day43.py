class Solution:
  def reverseWords(self, str):
    result = ''
    for word in str.split(' '):
        result += word[::-1] + ' '
    return result

print(Solution().reverseWords("The cat in the hat"))
# ehT tac ni eht tah