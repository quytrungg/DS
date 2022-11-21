class Node():
  def __init__(self, value, children=[]):
    self.value = value
    self.children = children

def is_symmetric(root):
    return True

tree = Node(4)
tree.children = [Node(3), Node(3)]
tree.children[0].children = [Node(9), Node(4), Node(1)]
tree.children[1].children = [Node(1), Node(4), Node(9)]
print(is_symmetric(tree))
# True