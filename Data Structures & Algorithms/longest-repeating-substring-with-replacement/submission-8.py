class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        maxF = 0
        count = {}
        # winlen - maxF <= k
        for r in range(len(s)):
            c = s[r]
            count[c] = count.get(c, 0) + 1
            maxF = max(maxF, count[c])

            while r - l + 1 - maxF > k:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        return longest