class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = collections.deque([root])
        non_null_count = 1
        while queue:
            head = queue.popleft()

            if not head:
                return non_null_count == 0
            non_null_count -= 1
            queue.append(head.left)
            queue.append(head.right)
            if head.left:
                non_null_count += 1
            if head.right:
                non_null_count += 1
        return True