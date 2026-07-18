class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = set()
        l = 0
        # pwwkew
        for r in range(len(s)):
            c = s[r]
            while c in seen:
                seen.remove(c)
                l = r
            seen.add(c)
            length = r - l + 1
            longest = max(longest, length)
        return longest

