class Solution:
    def rob(self, nums: List[int]) -> int:
        minusTwo, minusOne = 0, 0
        for n in nums:
            cur = max(minusTwo + n, minusOne)
            minusTwo = minusOne
            minusOne = cur
        return minusOne