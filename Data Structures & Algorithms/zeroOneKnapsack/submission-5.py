class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [0] * (capacity + 1)
        n = len(profit)

        for i in range(n):
            temp = [0] * (capacity + 1)
            for j in range(capacity + 1):
                skip = 0 + dp[j]
                take = float("-inf")
                if j >= weight[i]:
                    take = profit[i] + dp[j - weight[i]]
                temp[j] = max(skip, take)
            dp = temp
            
        return dp[capacity]



