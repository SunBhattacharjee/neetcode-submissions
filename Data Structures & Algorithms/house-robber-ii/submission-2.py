class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[n-1]
        return max(self.f(nums[1:]), self.f(nums[:n-1]))

    def f(self, nums: List[int]) -> int:
        minusTwo, minusOne = 0, 0
        for n in nums:
            cur = max(minusTwo + n, minusOne)
            minusTwo = minusOne
            minusOne = cur
        return minusOne
        