class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,v in enumerate(nums):
            if i > 0 and v == nums[i - 1]:
                continue
            target = 0 - v
            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = v + nums[l] + nums[r]
                if threeSum < target:
                    l += 1
                elif threeSum > target:
                    r -= 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

            return res