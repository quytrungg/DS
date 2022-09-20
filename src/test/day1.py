# question: given k and BST, find ceil and floor of k (floor: smaller but closest to k, ceil: larger but closest to k)

class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value
    
l = []

def findCeilingFloor(root_node, k, floor=None, ceil=None):
  if root_node == None:
      print((floor, ceil))
      return
  if root_node.value > k and (ceil == None or root_node.value < ceil):
      ceil = root_node.value
      findCeilingFloor(root_node.left, k, floor, ceil)
  elif root_node.value < k and (floor == None or root_node.value > floor):
      floor = root_node.value
      findCeilingFloor(root_node.right, k, floor, ceil)
      

root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

def PrintTree(r):
        if r.left:
            PrintTree(r.left)
        print( r.value),
        if r.right:
            PrintTree(r.right)

findCeilingFloor(root, 7)

# (4, 6)