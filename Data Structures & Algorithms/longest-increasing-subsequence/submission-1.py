class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        def f(i, last):
            if i == n:
                return 0
            skip = f(i+1, last)
            take = 0
            if last == -1 or nums[i] > nums[last]:
                take = 1 + f(i+1, i)
            return max(skip, take)

        # return f(0, -1)
        dp = [1] * (n)
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
            
        return max(dp)

        