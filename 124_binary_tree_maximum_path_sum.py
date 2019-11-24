# Divide and Conquer
# O(N)
# O(h) recursion stack so N for imbalanced tree, logN for balanced tree
# MAX() on the left_max right_max
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max = float('-inf')

        def max_gain(node):
            if not node:
                return 0
            left_max = max(max_gain(node.left), 0)
            right_max = max(max_gain(node.right), 0)

            new_route = right_max + left_max + node.val
            self.max = max(self.max, new_route)
            return node.val + max(left_max, right_max)

        max_gain(root)
        return self.max