class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0
        for i in range(len(nums)):
            cur = max(prev2 + nums[i], prev1)
            prev2 = prev1
            prev1 = cur
        return prev1
        