# https://leetcode.com/problems/validate-binary-search-tree/

# BFS Iterative
# O(N) visit every node once
# O(N) worst case hold all vertices in the queue.

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
from collections import deque
class Solution(object):
    def isValidBST(self, root):
        if not root:
            return True
        queue = collections.deque([(root, -float('inf'), float('inf'))])
        while queue:
            head, lower, upper = queue.popleft()
            if head.val <= lower or head.val >= upper:
                return False
            if head.left:
                queue.append((head.left, lower, head.val))
            if head.right:
                queue.append((head.right, head.val, upper))
        return True

# Rescursive Version
# O(n)
# O(n)

class Solution:
    def isValidBST(self, root):
        def DFS(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            left_valid = DFS(node.right, val, upper)
            right_valid = DFS(node.left, lower, val)
            return left_valid and right_valid
        return DFS(root)

# Inorder Traversal
# O(n)
# O(n)
class Solution(object):
    def isValidBST(self, root):
        stack = []
        prev = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True