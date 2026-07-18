class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = set()
        l = 0

        for r in range(len(s)):
            c = s[r]
            while c in seen:
                seen.remove(s[l])
                l += 1
            length = r - l + 1
            longest = max(longest, length)
            seen.add(c)
        return longest

