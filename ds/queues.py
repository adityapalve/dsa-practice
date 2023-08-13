# Implementing and figuring out queues
class Q:
  def __init__(self):
    self.q = []

  def foo(self):
    print('foo was called')
# Enqueue
  def enqueue(self, x):
    return self.q.append(x)
# Dequeue
  def dequeue(self, x):
    i = len(self.q)
    return self.q.pop(i)

l = []
l.append(1)
print(l)
l.append(2)
print(l)
l = l[-1::-1]
l.pop()
print(l)