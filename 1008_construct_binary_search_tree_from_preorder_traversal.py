# NO GLOBAL VERSION RECURSION
# O(N)
# O(N)
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(lower, upper, idx):
            if idx == len(preorder):
                return None, idx
            val = preorder[idx]
            if val < lower or val > upper:
                return None, idx
            idx += 1
            root = TreeNode(val)
            root.left, idx = helper(lower, val, idx)
            root.right, idx = helper(val, upper, idx)
            return root, idx
        ans, _ = helper(float('-inf'), float('inf'), 0)
        return ans

# O(N)
# O(N)

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.idx = 0
        def helper(lower, upper):
            if self.idx == n:
                return
            val = preorder[self.idx]
            if val < lower or val > upper:
                return None
            self.idx += 1
            root = TreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root
        n = len(preorder)
        return helper(float('-inf'), float('inf'))

# Iterative
# O(N)
# O(N)
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        n = len(preorder)
        if not n:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        for i in range(1, n):
            node = stack[-1]
            child = TreeNode(preorder[i])

            while stack and stack[-1].val < child.val:  # Backtrack to the right paretn
                node = stack.pop()

            if node.val < child.val:
                node.right = child
            else:
                node.left = child
            stack.append(child)
        return root