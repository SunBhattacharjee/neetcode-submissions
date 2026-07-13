class Solution:
    def rob(self, nums: List[int]) -> int:
        def act(i: int) -> int:
            if i >= len(nums):
                return 0
            skip = 0 + act(i+1)
            take = nums[i] + act(i+2)
            return max(skip, take)

        return act(0)
        