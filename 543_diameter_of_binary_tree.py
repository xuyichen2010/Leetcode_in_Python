# https://leetcode.com/problems/diameter-of-binary-tree/

# O(N) each node exactly once
# O(N) size of implicit call stack during DFS
class Solution:
    def diameterOfBinaryTree(self, root):
        self.best = 0
        def depth(root):
            if not root: return 0
            ansL = depth(root.left)
            ansR = depth(root.right)
            self.best = max(self.best, ansL + ansR)
            return 1 + max(ansL, ansR) #

        depth(root)
        return self.best