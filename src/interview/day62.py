class Solution():
  def fibonacci(self, n):
    if n <= 2:
        return 1
    return self.fibonacci(n-1) + self.fibonacci(n-2)

n = 9
print(Solution().fibonacci(n))
# 34