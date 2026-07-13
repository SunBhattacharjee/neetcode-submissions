class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(i):
            if i >= len(cost):
                return 0
            exp = 0
            if i >= 0:
                exp = cost[i]
            single_step = dfs(i+1)
            double_step = dfs(i+2)
            return exp + min(single_step, double_step)

        return dfs(-1)

        
        