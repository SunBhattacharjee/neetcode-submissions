class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = cost
        dp.append(0)
        dp.append(0)
        for i in range(n-1, -1, -1):
            dp[i] = dp[i] + min(dp[i+1], dp[i+2])

        return min(dp[0], dp[1])

            