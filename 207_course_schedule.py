# https://leetcode.com/problems/course-schedule/
# BFS Topological Search
# O(V+E)
# O(V+E)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        graph = collections.defaultdict(list)
        degrees = [0 for i in range(0, numCourses)]
        queue = collections.deque()
        for i, j in prerequisites:
            degrees[j] += 1
            graph[i].append(j)
        # push all nodes whose in-degrees are zero into the queue to start with
        counter = 0
        for i in range(0, numCourses):
            if degrees[i] == 0:
                queue.append(i)
        while queue:
            head = queue.popleft()
            counter += 1
            for neighbor in graph[head]:
                degrees[neighbor] -= 1
                if degrees[neighbor] == 0:
                    queue.append(neighbor)
        return counter == numCourses