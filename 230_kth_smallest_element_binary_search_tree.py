# O(H+k) defined by stack, contains at least H + k elements, H = logN or N depends on balanced or not
# O(H+k) same for the space
# Iteration

# FOLLOW-UP
# What if the BST is modified (insert/delete operations) often and you need
# to find the kth smallest frequently?
# How would you optimize the kthSmallest routine?

# https://leetcode.com/problems/kth-smallest-element-in-a-bst/solution/
# Ans0: Maintain a double-linked list where each node is pointed by an element in the tree
#       Reduce the time from insert/delet + search from O(2H + k) to O(H+k)
# Ans: 1. Add a counter in Tree class to store the num of nodes
#      2. Add a Dict to store the num of nodes for each subtree <node to nums>
#      Then use something like quick select e.g. if you are looking for the 4th you can
#      simply return if the 4th element is the root Reduce time complexity to O(h)
#      Time complexity for adding this sum counter is O(h)
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        if not root:
            return -1
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
        return -1

# Recursion
# O(n)
# O(N)
class Solution(object):
    def kthSmallest(self, root, k):
        res = []
        self.helper(root, res)
        return res[k-1]
    def helper(self, root, res):
        if not root:
            return None
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)