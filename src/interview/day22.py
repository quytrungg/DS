class Queue:
  def __init__(self):
    self.q = []
    self.top = 0
    self.bot = 0
    
  def enqueue(self, val):
    self.q.append(val)
    self.bot += 1
    return True

  def dequeue(self):
    self.top += 1
    return self.q[self.top-1]

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3