# Generating a Binary Tree
# Traversing Trees:- 1. BFS
#                    2. DFS
#

class Node:
    def __init__(self, key: int):
        self.right = None
        self.left = None
        self.key = key
#
# # Inserting value into a Node
# def insert(key):
#
#     return None
#
# # Deleting a Node
# def deleteNode(self,):
#     return None

class Traversal:
    # Inoder Traversal of the Tree
    # def __init__(self, node):
    #     self.root = node

    def inorderTraversal(self, root):
        res = []
        def traverse( root, res):
            if root:
                traverse(root.left, res)
                res.append(root.key)
                traverse(root.right, res)
        traverse(root, res)
        return res

    # Postorder Traversal of the Tree
    def postorderTraversal(self, root):
        res = []
        def traverse(root, res):
            if root:
                traverse(root.left, res)
                traverse(root.right, res)
                res.append(root.key)
        traverse(root, res)
        return res

    # Preoder Traversal of the Tree
    def preorderTraversal(self, root):
        res = []
        def traverse(root, res):
            if root:
                res.append(root.key)
                traverse(root.left, res)
                traverse(root.right, res)
        traverse(root, res)
        return res

tree = [1, 2, 4, 5]

# TODO: Make a function to create Trees.
root = Node(10)
root.left = Node(5)
root.right = Node(13)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(17)
root.right.left = Node(11)
obj                                                                                                                                                                                                                                                                                                                            = Traversal()
print(obj.inorderTraversal(root))
print(obj.postorderTraversal(root))
print(obj.preorderTraversal(root))