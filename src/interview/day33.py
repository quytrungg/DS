from itertools import count


class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def count_unival_subtrees(root):
    if not root.left and not root.right:
        return 1
    return (root.val == root.left.val and root.val == root.right.val) \
         + count_unival_subtrees(root.left) + count_unival_subtrees(root.right)

a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print(count_unival_subtrees(a))
# 5