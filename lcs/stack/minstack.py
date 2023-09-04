class MinStack():
  def __init__(self) -> None:
    self.stack = []

  def push(self, val:int)-> None:
    self.stack.append(val) 

  def pop(self)-> None:
    l = len(self.stack)
    self.stack.pop(l-1)

  def top(self)-> int:
    l = len(self.stack)
    return print(self.stack[l-1])
  
  def getMin(self)-> int:
    return print(min(self.stack)) 
  
  def show(self):
    return print(self.stack)
  
# o = MinStack()
# o.push(1)
# o.push(2)
# o.push(3)
# o.getMin()
# o.show()
# o.pop()
# o.top()
# o.getMin()
# o.show()

