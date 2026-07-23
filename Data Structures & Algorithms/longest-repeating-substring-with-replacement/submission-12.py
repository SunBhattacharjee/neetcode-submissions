class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        count = {}
        maxF = 0
        for r in range(len(s)):
            c = s[r]
            count[c] = 1 + count.get(c, 0)
            maxF = max(maxF, count[c])
            while l < r and r - l + 1 - maxF > k:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest