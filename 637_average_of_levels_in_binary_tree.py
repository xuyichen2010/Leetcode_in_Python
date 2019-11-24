# BFS
# O(N)
# O(M) the Width of the tree
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = collections.deque([root])
        res = []
        while queue:
            level_sum = 0
            level_count = len(queue)
            for _ in range(len(queue)):
                head = queue.popleft()
                level_sum += head.val
                if head.left:
                    queue.append(head.left)
                if head.right:
                    queue.append(head.right)
            res.append(level_sum / level_count)
        return res
# DFS
# O(N)
# O(H)
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        output = []
        depth = 0
        def trav(node, depth):
            depth += 1
            if len(output) < depth:
                output.append([])
            output[depth - 1].append(node.val)
            if node.left:
                trav(node.left, depth)
            if node.right:
                trav(node.right, depth)
        trav(root, depth)
        return [sum(x)/len(x) for x in output]