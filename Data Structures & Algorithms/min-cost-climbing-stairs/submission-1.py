class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(i: int, dp: List[int]) -> int:
            if i >= len(cost):
                return 0
            if dp[i] != -1:
                return dp[i]
            exp = 0
            if i >= 0:
                exp = cost[i]
            single_step = dfs(i+1, dp)
            double_step = dfs(i+2, dp)
            dp[i] = exp + min(single_step, double_step)
            return dp[i]
        
        dp = [-1] * (len(cost) + 1)
        return dfs(-1, dp)

        
        