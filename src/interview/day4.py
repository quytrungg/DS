# question: given n staircases, print out solutions number (fibonacci hidden)

# time comp: O(n)
def staircase2(n):
  if n < 2: return 1
  b = 1
  c = 1
  for _ in range(n-1):
    a = b + c
    c = b
    b = a
  return b

# time comp: O(2^n)
def staircase(n):
  if n < 2: return 1
  return staircase(n-1) + staircase(n-2)
  
print(staircase2(4))
# 5
print(staircase2(5))
# 8