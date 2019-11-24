# Naive sum
# O(mn)
# O(1)

# Naive Cache
# O(1)
# O(m^2n^2)

# O(mn) Constructing O(1) Accessing
# O(mn) space
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        n, m = len(matrix), len(matrix[0])
        self.dp = [[0 for j in range(m+1)]for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] + matrix[i-1][j-1] - self.dp[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.dp:
            return
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        return self.dp[row2][col2] - self.dp[row1-1][col2]- self.dp[row2][col1-1] + self.dp[row1-1][col1-1]
