# https://www.geeksforgeeks.org/level-order-tree-traversal/

# Method 1 (Use function to print a given level)

# O(n^2) time the worst case
# Because it takes O(n) for printGivenLevel when there's a skewed tree

# O(w) space where w is maximum width
# Max binary tree width is 2^h. Worst case when perfect binary tree
# Worst cas value 2^h is ceil(n/2)

# When tree is balanced BFS takes more space

from collections import deque

class Node :
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

    def printLevelOrder(self, root):
        h = self.height(root)
        for i in range (1, h+1):
            self.printGivenLevel(root, i)

    def height(self, node):
        if node is None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)
        return max(lheight, rheight) + 1

    def printGivenLevel(self, node, level):
        if node is None:
            return
        if level == 1:
            print(node.val)
        else:
            self.printGivenLevel(node.left, level-1)
            self.printGivenLevel(node.right, level-1)


