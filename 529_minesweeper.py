# BFS
# O(M*N) time complexity M = rol N = col
# O(M*N) ???? little tricky
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        queue = collections.deque()
        queue.append(click)
        adj_list = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        while queue:
            row, col = queue.popleft()
            if board[row][col] == 'M':
                board[row][col] = 'X'
            else:
                mine_count = 0
                for dx, dy in adj_list:
                    x = row + dx
                    y = col + dy
                    if not self.isValid(x, y, len(board), len(board[0])):
                        continue
                    if board[x][y] == 'M' or board[x][y] == 'X':
                        mine_count += 1
                if mine_count > 0:
                    board[row][col] = str(mine_count)
                else:
                    board[row][col] = 'B'
                    for dx, dy in adj_list:
                        x = row + dx
                        y = col + dy
                        if not self.isValid(x, y, len(board), len(board[0])):
                            continue
                        if board[x][y] == 'E':
                            queue.append([x, y])
                            board[x][y] = 'B'
        return board

    def isValid(self, x, y, x_bound, y_bound):
        return x >= 0 and y >= 0 and x < x_bound and y < y_bound

# DFS
# Switch the lines under if board[x][y] == 'E' to the following:
# self.updateBoard(board, [x, y])
