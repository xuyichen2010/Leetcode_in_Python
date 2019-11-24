 # Iterative DFS
# O(N) Each node exactly once
# O(N）Stack takes all element at skewed case
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        stack = []
        prev, smallest = None, None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev:
                prev.right = root
                root.left = prev
            else:
                smallest = root

            prev = root
            root = root.right
        if smallest:
            smallest.left = prev
            prev.right = smallest
        return smallest

# Recursive DFS
# O(N)
# O(N) call stack
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        head, _ = self.DFS(root)
        return head
    def DFS(self, root):
        head, tail = root, root
        if root.left:
            left_head, left_tail = self.DFS(root.left)
            left_tail.right = root
            root.left = left_tail
            head = left_head
        if root.right:
            right_head, right_tail = self.DFS(root.right)
            right_head.left = root
            root.right = right_head
            tail = right_tail
        head.left = tail
        tail.right = head
        return head, tail