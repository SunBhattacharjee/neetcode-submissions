class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+2)
        for i in range(2, n+2):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]