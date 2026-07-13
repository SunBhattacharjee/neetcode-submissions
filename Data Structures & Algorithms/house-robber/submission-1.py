class Solution:
    def rob(self, nums: List[int]) -> int:
        def act(i: int, dp: List[int]) -> int:
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            skip = 0 + act(i+1, dp)
            take = nums[i] + act(i+2, dp)
            dp[i] = max(skip, take)
            return dp[i]

        dp = [-1] * (len(nums) + 2)
        return act(0, dp)
        