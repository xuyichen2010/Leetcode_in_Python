# As we traverse, we compare the current node with its parent node to determine
# if it is consecutive. If not, we reset the length.

# O(N) every node
# O(N) call stack
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        return self.dfs(root, None, 0)
    def dfs(self, node, parent, length):
        if not node:
            return length
        if parent and node.val == parent.val + 1:
            length += 1
        else:
            length = 1
        left_max = self.dfs(node.left, node, length)
        right_max = self.dfs(node.right, node, length)
        return max(left_max, right_max, length)

