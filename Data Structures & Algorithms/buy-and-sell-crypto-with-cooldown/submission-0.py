class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def f(i, buy, dp):
            if i >= len(prices):
                return 0
            if dp[i][buy] != -1:
                return dp[i][buy]
            # sell
            profit = prices[i] + f(i+2, 1, dp)
            if buy == 1:
                profit = max(profit, -prices[i] + f(i+1, 0, dp))
                
            dp[i][buy] = profit
            return dp[i][buy]

        dp = [[-1] * 2 for _ in range(len(prices))]
        return f(0, 1, dp)
        