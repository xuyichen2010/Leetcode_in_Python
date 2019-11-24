# https://leetcode.com/problems/binary-tree-paths/solution/

# Divide and Conqure
# O(n) visit each node exactly once
# O(n)

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]

        l_path = self.binaryTreePaths(root.left)
        r_path = self.binaryTreePaths(root.right)
        paths = []
        for path in l_path:
            paths.append(str(root.val) + '->' + path)
        for path in r_path:
            paths.append(str(root.val) + '->' + path)
        return paths
# DFS Recursion

class Solution(object):
    def binaryTreePaths(self, root):
        if root is None:
            return []

        result = []
        self.dfs(root, [str(root.val)], result)
        return result

    def dfs(self, node, path, result):
        if node.left is None and node.right is None:
            result.append('->'.join(path))
            return
        if node.left:
            path.append(str(node.left.val))
            self.dfs(node.left, path, result)
            path.pop()
        if node.right:
            path.append(str(node.right.val))
            self.dfs(node.right, path, result)
            path.pop()

# Recursion
# Top to down
# O(n)
# O(n) call stack
class Solution:
    def binaryTreePaths(self, root):
        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:  # if reach a leaf
                    paths.append(path)  # update paths
                else:
                    path += '->'  # extend the current path
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)

        paths = []
        construct_paths(root, '')
        return paths

# Iteration
# Top to Bottom
class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []

        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))

        return paths