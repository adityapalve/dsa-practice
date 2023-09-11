class Node():
  def __init__(self, data) -> None:
    self.data = data 
    self.next = None

class Ll():
  def __init__(self) -> None:
    self.head = None

  def insert(self, node):
    curr = self.head 
    while curr.next:
      curr = curr.next
    
    curr.next = node

  def delete(self, val):
    if self.head == None:
      return

    if self.head.data == val:
      self.head = self.head.next 

    curr = self.head

    while curr.next:
      # 
      if curr.next.data == val:
        curr.next = curr.next.next
        return
      curr = curr.next

  
  def show(self):
  
  