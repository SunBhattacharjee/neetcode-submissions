class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def f(i, j):
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1
            return f(i-1, j) + f(i, j-1)
        
        if m == 1 or n == 1:
            return 1
        dp = [[0] * (n+1) for _ in range(m+1)]
        # dp[0][0] = 1
        for i in range(1, m+1):
            dp[i][1] = 1
        for j in range(1, n+1):
            dp[1][j] = 1
        dp[1][1] = 0
        for i in range(2, m+1):
            for j in range(2, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m][n]
                

        