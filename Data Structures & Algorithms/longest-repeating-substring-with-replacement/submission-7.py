class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        longest = 0
        maxF = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])
            while (r - l + 1) - maxF > k:
                count[s[l]] = count[s[l]] - 1
                l += 1
            longest = max(longest, r - l + 1)

        return longest
            