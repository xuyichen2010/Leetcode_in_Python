# O(N + E) == O(N) because in a tree # of edges is always 1 less than the # of nodes
# O(N)

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = collections.defaultdict(list)
        self.buildGraph(None, root, graph)
        return self.BFS(graph, target, K)

    def buildGraph(self, parent, child, graph):
        if parent and child:
            graph[parent.val].append(child.val)
            graph[child.val].append(parent.val)
        if child.left:
            self.buildGraph(child, child.left, graph)
        if child.right:
            self.buildGraph(child, child.right, graph)

    def BFS(self, graph, target, K):
        queue = collections.deque([(target.val, 0)])
        visited = set()
        ans = []
        while queue:
            head, distance = queue.popleft()
            if head in visited:
                continue
            visited.add(head)
            if distance == K:
                ans.append(head)
            elif distance < K:
                for neighbor in graph[head]:
                    queue.append((neighbor, distance + 1))
        return ans