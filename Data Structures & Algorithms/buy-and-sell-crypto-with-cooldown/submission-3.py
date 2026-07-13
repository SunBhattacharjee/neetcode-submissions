class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def f(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            skip = f(i+1, buying)
            if buying:
                buy = f(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, skip)
            else:
                sell = f(i+2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, skip)

            return dp[(i, buying)]

        return f(0, True)
