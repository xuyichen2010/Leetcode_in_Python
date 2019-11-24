# Assumptions:
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.

# ASK CLARIFYING QUESTION: IF ANY ONE OF THEM IS FINE OR DO YOU WANT THE MINIMUM?
# Build Graph O(n*k) n = num of words k = longest words char num
# Torp Sort O(V+E) V = num of unique chars E = num of word pairs (num of words - 1)
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = self.build_graph(words)
        result = self.top_sort(graph)

        return "" if len(result) != len(graph) else ''.join(result)

    def build_graph(self, words):
        graph = {}
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()

        for i in range(len(words) - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    break
        return graph

    def top_sort(self, graph):
        in_degrees = {node: 0 for node in graph}

        for node in graph:
            for neighbor in graph[node]:
                in_degrees[neighbor] += 1

        queue = collections.deque()

        for i in in_degrees:
            if in_degrees[i] == 0:
                queue.append(i)
        result = []
        while queue:
            head = queue.popleft()
            result.append(head)
            for neighbor in graph[head]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)
        return result