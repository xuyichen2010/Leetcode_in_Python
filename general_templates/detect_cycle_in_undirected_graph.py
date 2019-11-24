# https://www.geeksforgeeks.org/detect-cycle-undirected-graph/
from collections import defaultdict

class Graph:
    def __init__(self, num_of_vertices):
        self.V = num_of_vertices
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def isCyclicUtil(self, v, visited, parent):
        visited[v] = True

        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.isCyclicUtil(neighbour, visited, v):
                    return True
            elif parent != neighbour:
                return True
        return False

    def isCyclic(self):
        visited = [False] * self.V
        for i in range(self.V):
            if visited[i] == False:
                if self.isCyclicUtil(i, visited, -1) == True:
                    return True
        return False


# Create a graph given in the above diagram
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)

if g.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle ")
g1 = Graph(3)
g1.addEdge(0, 1)
g1.addEdge(1, 2)

if g1.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle ")