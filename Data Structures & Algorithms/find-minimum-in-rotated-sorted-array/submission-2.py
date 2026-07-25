class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        arrMin = nums[l]
        while l <= r:
            if nums[l] < nums[r]:
                arrMin = min(arrMin, nums[l])
                break
            mid = (l + r) // 2
            arrMin = min(arrMin, nums[mid])
            if nums[mid] >= nums[l]:
                l += 1
            else:
                r -= 1
        return arrMin