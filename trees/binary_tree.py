
#Inverting a Binary Tree 
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def shape(self):
        return [self.left.val, self.val, self.right.val]


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(node):

            # If there is a node
            if node:

                # Invert the left subtree and the right subtree
                left, right = invert(node.left), invert(node.right)

                # Swap the head of the left subtree with the head of the right subtree
                node.left, node.right = right, left

            return node

        return invert(root)


a = TreeNode(1, None, None)
c = TreeNode(8, None, None)
b = TreeNode(5, None, c)
tree = TreeNode(10, a, b)

print(tree.shape())