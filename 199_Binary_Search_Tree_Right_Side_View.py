# https://leetcode.com/problems/binary-tree-right-side-view/solution/

# Use BFS Level Order Traversal
# O(n) Visit each node exactly once
# O(n) Worst space in queue when visiting the last layer which is 0.5N in the worst case (A Complete Binary Tree)

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        while queue:
            queue_size = len(queue)
            for i in range(queue_size):
                head = queue.popleft()
                if i == queue_size - 1:
                    res.append(head.val)
                if head.left:
                    queue.append(head.left)
                if head.right:
                    queue.append(head.right)
        return res

# DFS
# O(n) directed acyclic graph. visit each node exactly once
# O(n) recursion call stack space

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        self.DFS(root, 0, res)
        return [i[-1] for i in res]

    def DFS(self, node, level, res):
        if not node:
            return
        if len(res) <= level:
            res.append([])
        res[level].append(node.val)
        self.DFS(node.left, level + 1, res)
        self.DFS(node.right, level + 1, res)