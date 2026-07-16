class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        res = 0
        for r in range(1, len(s) - 1):
            while s[r] in seen:
                seen.remove(s[r])
                l += 1
            seen.add(s[r])
        return res
        