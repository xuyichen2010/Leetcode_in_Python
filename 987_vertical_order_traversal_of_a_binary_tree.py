# [x ,y]
# if the node shows up at a higher level it will be added first
# if two nodes are on the same level then they will be sorted
# Do not fully sort a vertical column! That will fail testcases.

# O(NlogN) sort
# O(N)
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        seen = collections.defaultdict(lambda:collections.defaultdict(list))
        def dfs(node, x, y):
            if not node:
                return
            seen[x][y].append(node)
            dfs(node.left, x-1, y+1)
            dfs(node.right, x+1, y+1)
        dfs(root, 0, 0)
        ans = []
        for x in sorted(seen):
            report = []
            for y in sorted(seen[x]):
                report.extend(sorted(node.val for node in seen[x][y]))
            ans.append(report)
        return ans