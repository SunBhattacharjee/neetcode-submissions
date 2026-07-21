class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        window = {}
        l = 0
        maxF = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            maxF = max(maxF, window[c])
            while l < r and (r - l + 1) - maxF > k:
                window[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        return longest