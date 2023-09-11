
class Node():
  def __init__(self, data=None) -> None:
    self.data = data
    self.next = None


class LinkedList():
  def __init__(self) -> None:
    self.head = None

  def insert(self, ele):
    if self.head == None:
      self.head = ele 

    else:
      curr = self.head
      while curr.next:
        curr = curr.next

      curr.next = ele


  def delete(self, val):
    if self.head == None:
      return

    if self.head.data == val    
      self.head = self.head.next

    curr = self.head
    while curr.next:
      if curr.next.data == val:
        curr.next = curr.next.next
        return
      curr = curr.next

  def show(self, val):

    curr = self.head   
    while curr:
      print(curr.data)

      curr = curr.next


