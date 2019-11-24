# O(N)
# O(N)

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        MIN, MAX = 0, 0
        index_to_node = collections.defaultdict(list)
        queue = collections.deque()
        queue.append((root, 0))
        res = []
        while queue:
            node, index = queue.popleft()
            index_to_node[index].append(node.val)
            if node.left:
                queue.append((node.left, index - 1))
                MIN = min(MIN, index - 1)
            if node.right:
                queue.append((node.right, index + 1))
                MAX = max(MAX, index + 1)

        for i in range(MIN, MAX + 1):
            res.append(index_to_node[i])

        return res