class minStack(object):
  def __init__(self):
    pass

  def push(self, x):
    pass

  def pop(self):
    pass

  def top(self):
    pass

  def getMin(self):
    pass

x = minStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
# -3
x.pop()
print(x.top())
# 0
print(x.getMin())
# -2