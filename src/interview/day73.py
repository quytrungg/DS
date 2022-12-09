class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None

def is_palindrome(node):
    if node == None:
        return True
    return False

node = Node('a')
node.next = Node('b')
node.next.prev = node
node.next.next = Node('b')
node.next.next.prev = node.next
node.next.next.next = Node('a')
node.next.next.next.prev = node.next.next

print(is_palindrome(node))
# True