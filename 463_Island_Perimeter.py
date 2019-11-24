class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        def isBoundary(grid, x, y):
            count = 0
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                c_x = x + dx
                c_y = y + dy
                if c_x < 0 or c_y < 0 or c_x >= len(grid) or c_y >= len(grid[0]) or grid[c_x][c_y] == 0:
                    count += 1
            return count
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += isBoundary(grid, i, j)
        return res