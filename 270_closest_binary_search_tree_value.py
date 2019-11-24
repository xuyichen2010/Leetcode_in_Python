# https://leetcode.com/problems/closest-binary-search-tree-value/discuss/70395/Python-different-recursive-solutions.

# Naive In-order Traversal
# O(N)
# O(N)
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(r: TreeNode):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        return min(inorder(root), key=lambda x: abs(target - x))


# BST non-recursive
# Find lower and upper bound and compare
# O(H+k) one goes from root down to a leaf
# O(1)
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        upper = root.val
        lower = root.val
        while root:
            if target > root.val:
                lower = root.val
                root = root.right
            elif target < root.val:
                upper = root.val
                root = root.left
            else:
                return root.val
        return min(lower, upper, key=lambda k: abs(target - k))
# O(H+k)
# O(H) if the tree is not balanced
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        stack = []
        prev = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev <= target and target < root.val:
                return min(prev, root.val, key=lambda k: abs(target - k))
            prev = root.val
            root = root.right
        return prev
# BST Recursive
# O(H)
# O(1)
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        a = root.val
        kid = None
        if target < root.val:
            kid = root.left
        elif target > root.val:
            kid = root.right
        if not kid:
            return a
        b = self.closestValue(kid, target)
        return min(a, b, key=lambda k: abs(target - k))


# works for normal binary tree
# Back-tracking
# O(n) time
# O(1) space
def closestValue1(self, root, target):
    if not root:
        return 0
    self.res = root.val
    self.findClosest(root, target)
    return self.res


def findClosest(self, root, target):
    if root:
        if abs(root.val - target) == 0:
            self.res = root.val
            return  # backtracking
        if abs(root.val - target) < abs(self.res - target):
            self.res = root.val
        self.findClosest(root.left, target)
        self.findClosest(root.right, target)