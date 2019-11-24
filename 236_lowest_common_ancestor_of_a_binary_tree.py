# Nodes have to exist in the tree
# O(N)
# O(N) tree might be not balanced
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root == p or root == q:
            return root
        left_node = self.lowestCommonAncestor(root.left, p, q)
        right_node = self.lowestCommonAncestor(root.right, p, q)
        if left_node and right_node:
            return root
        elif left_node:
            return left_node
        elif right_node:
            return right_node
        return None

# Nodes might not in the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # write your code here
        a, b, res = self.LCA(root, p, q)
        if a and b:
            return res
        else:
            return None

    def LCA(self, root, p, q):
        if root is None:
            return False, False, None

        l_a, l_b, l_node = self.LCA(root.left, p, q)
        r_a, r_b, r_node = self.LCA(root.right, p, q)

        a = l_a or r_a or root == p
        b = l_b or r_b or root == q

        if l_node and r_node or root == p or root == q:
            return a, b, root
        if l_node:
            return a, b, l_node
        if r_node:
            return a, b, r_node
        return a, b, None