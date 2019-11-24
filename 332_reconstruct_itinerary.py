# O(NlogD) D = maximum outgoing degree of a vertex
# O(V + E)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Constructing the graph
        graph = {}
        for src, dst in tickets:
            if src in graph:
                graph[src].append(dst)
            else:
                graph[src] = [dst]

        # Satisfying the lexical order condition
        # Reverse to avoid O(n) cost for pop(0)
        for src in graph.keys():
            graph[src].sort(reverse=True)

        stack = ["JFK"]
        res = []
        # Appending the final destination first
        while len(stack) > 0:
            head = stack[-1]
            if head in graph and len(graph[head]) > 0:
                stack.append(graph[head].pop())
            else:
                res.append(stack.pop())
        return res[::-1]