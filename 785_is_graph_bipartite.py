# O(N+E) explore each node once and traverse all its edges
# O(N) color

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        for node in range(len(graph)):
            if node in color:
                continue
            stack = [node]
            color[node] = 0
            while stack:
                node = stack.pop()
                for neighbour in graph[node]:
                    if neighbour not in color:
                        stack.append(neighbour)
                        color[neighbour] = color[node] ^ 1
                    elif color[neighbour] == color[node]:
                        return False
        return True