# question: given 2 linked list, find intersect linked list

def intersection(a, b):
  while a != None:
    cur = b
    while cur != None:
      if cur.val == a.val and cur.next.val == a.next.val:
        return a
      cur = cur.next
    a = a.next
  return None

class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
  def prettyPrint(self):
    c = self
    while c:
      print(c.val)
      c = c.next

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

c = intersection(a, b)
c.prettyPrint()
# 3 4