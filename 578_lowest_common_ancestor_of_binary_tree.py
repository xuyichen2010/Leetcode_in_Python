# Leetcode case
# Divide and Counqur

# O(n) every node
# O(n) call stack in-balanced tree
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return
        if root == p or root == q:
            return root

        left_ancestor = self.lowestCommonAncestor(root.left, p, q)
        right_ancestor = self.lowestCommonAncestor(root.right, p, q)

        if left_ancestor and right_ancestor:
            return root
        if left_ancestor:
            return left_ancestor
        if right_ancestor:
            return right_ancestor
        return
# If the node could be not on the tree
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
    
# Iterate with a parent Node
class Solution:

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:

            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q