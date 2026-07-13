class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        step1 = cost[0]
        step2 = 0
        for i in range(1, n+1):
            stepCost = nums[i-1]
            cur = max(prev2, prev1) + stepCost
            step2 = step1
            step1 = cur
        return step1


        


