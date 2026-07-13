class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        longest = 1
        myset = set(nums)
        for n in nums:
            if not (n - 1) in myset:
                count = 1
                while (n + count) in myset:
                    count += 1
                    longest = max(longest, count)
        
        return longest