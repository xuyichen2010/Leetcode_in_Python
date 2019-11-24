# Recursion DFS

# O(N)
# O(H) O(N) for the worst case
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.dfs(root)

    def dfs(self, node):
        if not node:
            return 0
        left_height = self.dfs(node.left)
        right_height = self.dfs(node.right)
        return max(left_height, right_height) + 1

# Iterative DFS

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = []
        height = 0
        max_h = 0
        while stack or root:
            while root:
                height += 1
                stack.append((root, height))
                root = root.left
            root, height = stack.pop()
            max_h = max(max_h, height)
            root = root.right

        return max_h
# BFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = collections.deque([root])
        height = 0
        while queue:
            height += 1
            for _ in range(len(queue)):
                head = queue.popleft()
                if head.left:
                    queue.append(head.left)
                if head.right:
                    queue.append(head.right)
        return height