# DFS
# O(h * 2^h) where h is the height of the tree which is N in the worst case
# O(h * 2^h) for the output array res
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        height = self.getHeight(root)
        width = 2 ** height - 1
        res = [[''] * width for i in range(height)]
        self.update_output(root, 0, 0, width - 1, res)
        return res

    def update_output(self, node, row, left, right, res):
        if not node:
            return
        mid = (left + right) // 2
        res[row][mid] = str(node.val)
        print(node.val, row, res)
        self.update_output(node.left, row + 1, left, mid - 1, res)
        self.update_output(node.right, row + 1, mid + 1, right, res)

    def getHeight(self, root):
        if not root:
            return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1