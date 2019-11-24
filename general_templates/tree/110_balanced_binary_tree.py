# O(n) need to visit every node
# O(n) could be unbalanced

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        res, _ = self.helper(root)
        return res
    def helper(self, root):
        if root is None:
            return True, 0
        left_res, left_depth = self.helper(root.left)
        right_res, right_depth = self.helper(root.right)
        if not left_res or not right_res or abs(left_depth - right_depth) > 1:
            return False, 0
        return True, max(left_depth, right_depth)+1