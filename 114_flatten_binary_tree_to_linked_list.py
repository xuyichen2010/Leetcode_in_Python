# https://www.jiuzhang.com/solution/flatten-binary-tree-to-linked-list/#tag-highlight-lang-python

# O(n) n = num of nodes
# O(1) space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    lastNode = None
    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return
        if self.lastNode:
            self.lastNode.right = root
            self.lastNode.left = None

        self.lastNode = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)

# Recursive

def __init__(self):
    self.prev = None

def flatten(self, root):
    if not root:
        return None
    self.flatten(root.right)
    self.flatten(root.left)

    root.right = self.prev
    root.left = None
    self.prev = root

# Divide and Conqur
class Solution:

    def flatten(self, root):
        self.helper(root)

    # restructure and return last node in preorder
    def helper(self, root):
        if root is None:
            return None

        left_last = self.helper(root.left)
        right_last = self.helper(root.right)

        # connect
        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None

        return right_last or left_last or root