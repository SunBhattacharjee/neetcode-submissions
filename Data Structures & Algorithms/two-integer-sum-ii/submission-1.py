class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        while l < r:
            twoSum = nums[l] + nums[r]
            if twoSum < target:
                l += 1
            elif twoSum > target:
                r -= 1
            else:
                return [l+1,r+1]