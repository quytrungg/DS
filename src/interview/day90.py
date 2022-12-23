from collections import deque

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __str__(self):
    return

tree = Node('a')
tree.left = Node('b')
tree.right = Node('c')
tree.left.left = Node('d')
tree.left.right = Node('e')
tree.right.left = Node('f')
tree.right.right = Node('g')

print(tree)
# a
# bc
# defg