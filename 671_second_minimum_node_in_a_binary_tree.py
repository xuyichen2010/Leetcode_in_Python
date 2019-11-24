# O(N) visit each node in the worst case
# O(N) call stack for DFS
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.ans = float('inf')
        min_val = root.val

        def DFS(node):
            if not node:
                return
            if node.val > min_val and node.val < self.ans:
                self.ans = node.val
            elif node.val == min_val:
                DFS(node.left)
                DFS(node.right)

        DFS(root)
        return self.ans if self.ans != float('inf') else -1
