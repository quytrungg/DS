class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

def is_bst(root):
    if not root or not root.left or not root.right:
        return True
    if root.key > root.right.key or root.key < root.left.key:
        return False
    return is_bst(root.left) and is_bst(root.right)

a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)
print(is_bst(a))

#    5
#   / \
#  3   7
# / \ /
#1  4 6