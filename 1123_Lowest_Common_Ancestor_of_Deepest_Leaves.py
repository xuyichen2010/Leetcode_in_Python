# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/discuss/334577/JavaC%2B%2BPython-Two-Recursive-Solution
# O(n) for one path
# O(n) for recursion management
# helper function return the subtree height and lca and at the same time.
# null node will return depth 0,
# leaves will return depth 1.

def lcaDeepestLeaves(self, root):
    def helper(root):
        if not root: return 0, None
        h1, lca1 = helper(root.left)
        h2, lca2 = helper(root.right)
        if h1 > h2: return h1 + 1, lca1
        if h1 < h2: return h2 + 1, lca2
        return h1 + 1, root

    return helper(root)[1]