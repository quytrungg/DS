class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

result = []
def valuesAtHeight(root, height):
    if not root:
        return
    valuesAtHeight(root.left, height-1)
    if height == 1:
        result.append(root.value)
    valuesAtHeight(root.right, height-1)

#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
valuesAtHeight(a, 3)
print(result)

def sum1n(n):
    if n == 0:
        return 0
    return n + sum1n(n-1)

print(sum1n(10))
# [4, 5, 7]