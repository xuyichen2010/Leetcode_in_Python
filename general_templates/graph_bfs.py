# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

# unlike trees, graphs may contain cycles, so we may come to the same node again.
# To avoid processing a node more than once, we use a boolean visited array.

# For simplicity, it is assumed that all vertices are reachable from the starting vertex.

from collections import defaultdict
from collections import deque

class Graph:
    def __init__ (self, V):
        # default dictionary to store the graph
        self.graph = defaultdict(list)
        self.vertices = V
    # function used to add an edge to the graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):

        visited = [False] * (len(self.graph))

        queue = deque()

        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.popleft()
            # Do stuff here
            print(s, end = " ")

            # Check all neighbours
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
if __name__ == "__main__":
    g = Graph([0, 1, 2, 3])
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.BFS(2)
