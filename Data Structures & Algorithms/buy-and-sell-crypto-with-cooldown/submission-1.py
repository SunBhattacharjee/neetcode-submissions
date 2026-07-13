class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def f(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in dp:
                return dp[(i, buy)]
            
            skip = f(i+1, buy)
            if buy:
                buy = f(i+1, not buy) - prices[i]
                dp[(i, buy)] = max(buy, skip)
            else:
                sell = f(i+2, not buy) + prices[i]
                dp[(i, buy)] = max(sell, skip)

            return dp[(i, buy)]

        return f(0, True)
