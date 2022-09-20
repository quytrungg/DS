count = 0

def staircase(n):
  if n < 2: return 1
  return staircase(n-1) + staircase(n-2)
  
print(staircase(4))
# 5
print(staircase(5))
# 8