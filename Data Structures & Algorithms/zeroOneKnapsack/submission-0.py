class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        def dfs(ind, cap, wt, val, cache):
            if ind == len(wt):
                return 0
            
            if cache[ind][cap] != -1:
                return cache[ind][cap]

            # skip
            maxProfit = dfs(ind + 1, cap, wt, val, cache)

            # take
            rem = cap - wt[ind]
            if rem >= 0:
                take = val[ind] + dfs(ind + 1, rem, wt, val, cache)
                cache[ind][cap] = max(maxProfit, take)

            return cache[ind][cap]

        dp = [[-1] * (capacity+1) for _ in range(len(weight))]
        return dfs(0, capacity, weight, profit, dp)


