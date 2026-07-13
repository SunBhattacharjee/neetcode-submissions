class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+2)
        for i in range(2, n+2):
            skip = dp[i-1]
            take = nums[i-2] + dp[i-2]
            dp[i] = max(skip, take)
        return dp[n+1]