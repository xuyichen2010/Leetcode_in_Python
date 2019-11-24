# O(h) space where h is maximum height
# h of balanced binary tree is logn.
# Worst case occurs for skewed tree at n

# When tree is not balanced DFS takes more space
# 1. DFS need recursive and requires function call overheads
# 2. DFS start from leaves, so answer closer to the leaves
class Node(object):
    def __init__(self, v):
        self.left = None
        self.right = None
        self.value = v
'''
In case of binary search trees (BST), 
Inorder traversal gives nodes in non-decreasing order. 
To get nodes of BST in non-increasing order, 
a variation of Inorder traversal where Inorder traversal s reversed can be used.
'''
def inorder(self, root):
    if root:
        self.inorder(root.left)
        print(root.value)
        self.inorder(root.right)
'''
Preorder traversal is used to create a copy of the tree. 
Preorder traversal is also used to get prefix expression on of an expression tree. 
Please see http://en.wikipedia.org/wiki/Polish_notation to know why prefix expressions are useful.
'''
def preorder(self, root):
    if root:
        print(root.value)
        self.inorder(root.left)
        self.inorder(root.right)
'''
Post-order traversal is used to delete the tree.
 Please see the question for deletion of tree for details. 
 https://www.geeksforgeeks.org/write-a-c-program-to-delete-a-tree/
 Post-order traversal is also useful to get the postfix expression of an expression tree. 
 Please see http://en.wikipedia.org/wiki/Reverse_Polish_notation to for the usage of postfix expression.
'''


def postorder(self, root):
    if root:
        self.inorder(root.left)
        self.inorder(root.right)
        print(root.value)

# iteration Inorder
def inorderTraversal(self, root):
    stack = []
    dummy = Node(-1)
    dummy.right = root
    stack.append(dummy)
    res = []
    while stack:
        node = stack.pop()
        node = node.right
        while node:
            stack.append(node)
            node = node.left
        if stack:
            res.append(stack[-1].val)
    return res