# question: given a linked list, remove string nodes that sum up to 0

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def removeConsecutiveSumTo0(node):
  if node == None: return None
  sum = 0
  temp = Node(-1)
  cur = temp
  cur.next = node
  while cur.next != None:
    cur2 = cur.next
    sum += cur2.value
    while sum != 10:
      cur2 = cur2.next
      sum += cur2.value
    cur2 = cur2.next
    cur.next = cur2
    cur = cur.next
  return node

node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeConsecutiveSumTo0(node)
while node:
  print(node.value)
  node = node.next
# 10