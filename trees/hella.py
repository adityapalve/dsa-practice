
class Node:
  def __init__(self, val=None, left=None, right=None):
    self.val = val
    self.left = self._to_node(left)
    self.right = self._to_node(right)

  def _to_node(self, attr):
    if isinstance(attr, Node):
      return attr
    return Node(attr) if attr is not None else None
    
  def inorder(self, root):
    if root is None:
      return

    self.inorder(root.left)
    print(root.val)
    self.inorder(root.right)

  def preorder(self, root):
    if root == None:
      return
    
    print(root.val)
    self.preorder(root.left)
    self.preorder(root.right)

  def postorder(self, root):
    if root == None:
      return
    
    self.postorder(root.left)
    self.postorder(root.right)
    print(root.val)

  def debug(self):
      print(
        f'val: {self.val}', 
        f'left: {self.left}', 
        f'right: {self.right}'
      )

# tree = [1, 2, 4, 5]
l = Node(5, None, None)
r = Node(13, 4, 2)

'''
          10
        /   \
      5     13
          /   \  
         4     2 
'''
o = Node(10, l, r)


# print(o)
# print(o.debug())
# print(o.left.debug())
print("        10")
print("      /   \\")
print("    5     13")
print("        /   \\")
print("       4     2")
print('Inorder:')
o.inorder(o)
print('---')
print('Preorder:')
o.preorder(o)
print('---')
print('Postorder:')
o.postorder(o)

