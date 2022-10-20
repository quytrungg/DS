class Solution:
  def buddyStrings(self, A, B):
    count = 2
    length = len(A) if len(A) < len(B) else len(B)
    for i in range(length):
        if A[i] != B[i]:
            count -= 1
    return len(A) == len(B) and count == 0

print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False