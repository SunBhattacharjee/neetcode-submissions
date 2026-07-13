class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float("inf")] * (amount + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 0
            
        for j in range(amount+1):
            if j % coins[0] == 0:
                dp[0][j] = j//coins[0]

        for i in range(1, n):
            for j in range(amount+1):
                skip = dp[i-1][j]
                take = dp[i][j]
                if j >= coins[i]:
                    take = 1 + dp[i][j - coins[i]]
                dp[i][j] = min(skip, take)

        return dp[n-1][amount] if dp[n-1][amount] != float("inf") else -1