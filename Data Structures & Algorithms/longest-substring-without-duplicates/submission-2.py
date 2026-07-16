class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        res = 0
        if len(s) == 1:
            return 1
        for r in range(1, len(s) - 1):
            if s[r] not in seen:
                res += 1
                seen.add(s[r])
            else:
                l = r + 1
        return res
        