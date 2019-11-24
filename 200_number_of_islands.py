# BFS (Better than DFS in a sense that worst space for DFS is O(M*N)
# O(M*N) M = rows N = cols
# O(min(M,N)) when the grid is filled with lands, the size of queue can grow up to min(M,N)
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Traverse through the matrix
        # For each grid perfrom BFS and mark visited node as 0
        # Increment counter for each finished BFS
        num_of_islands = 0
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited and grid[i][j] == '1':
                    self.BFS(grid, i, j, visited)
                    num_of_islands += 1
                # Bfs Traverse
                # Increment Counter
        return num_of_islands

    def BFS(self, grid, i, j, visited):
        queue = deque([(i, j)])
        visited.add((i, j))
        while queue:
            i, j = queue.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x = i + dx
                y = j + dy
                if self.isValid(x, y, len(grid), len(grid[0])):
                    if (x, y) not in visited and grid[i][j] == '1':
                        queue.append((x, y))
                        visited.add((x, y))
        return

    def isValid(self, x, y, x_bound, y_bound):
        return x >= 0 and y >= 0 and x < x_bound and y < y_bound