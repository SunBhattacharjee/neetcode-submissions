class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
                continue
            profit = prices[r] - prices[l]
            maxProfit = max(profit, maxProfit)
        return maxProfit