# https://leetcode.com/problems/binary-search-tree-iterator/solution/

# Naive way flatten to sorted list using inorder and keep counter
# O(N)
# O(N)
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nodes_sorted = []
        self.index = -1
        self._inorder(root)

    def _inorder(self, root):
        if not root:
            return
        self._inorder(root.left)
        self.nodes_sorted.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        self.index += 1
        return self.nodes_sorted[self.index]

    def hasNext(self) -> bool:

        return self.index + 1 < len(self.nodes_sorted)
# O(n) for next
# O(h) for stack space for tree

class BSTIterator(object):

    def __init__(self, root):
        dummy = TreeNode(-1)
        dummy.right = root
        self.stack = [dummy]
        self.next()

    def next(self):
        head = self.stack.pop()
        next_node = head
        if head.right:
            head = head.right
            while head:
                self.stack.append(head)
                head = head.left
        return next_node.val

    def hasNext(self):
        return bool(self.stack)