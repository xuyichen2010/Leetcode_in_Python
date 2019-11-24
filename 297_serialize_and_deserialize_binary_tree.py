# O(n)
# O(n)
class Codec:
    def serialize(self, root):
        if not root:
            return
        queue = collections.deque([root])
        res = []
        while queue:
            head = queue.popleft()
            if not head:
                res.append('None')
                continue
            res.append(head.val)
            queue.append(head.left)
            queue.append(head.right)

        return ','.join(str(k) for k in res)

    def deserialize(self, data):
        if not data:
            return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        queue = collections.deque([root])
        i = 1
        while queue and i < len(nodes):
            head = queue.popleft()
            if nodes[i] != 'None':
                temp = TreeNode(int(nodes[i]))
                head.left = temp
                queue.append(head.left)
            i += 1
            if nodes[i] != 'None':
                temp = TreeNode(int(nodes[i]))
                head.right = temp
                queue.append(head.right)
            i += 1
        return root

# DFS
# O(n)
# O(n)
class Codec:

    def serialize(self, root):
        def helper(root, res):
            if not root:
                res.append('None')
            else:
                res.append(str(root.val))
                helper(root.left, res)
                helper(root.right, res)
        res = []
        helper(root, res)
        return ','.join(res)

    def deserialize(self, data):
        def helper(data):
            if data[0] == 'None':
                data.popleft()
                return None
            root = TreeNode(data.popleft())
            root.left = helper(data)
            root.right = helper(data)
            return root
        data = data.split(',')
        return helper(collections.deque(data))