class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniq = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in uniq:
                uniq.remove(s[l])
                l += 1
            uniq.add(s[r])
            longest = max(longest, r - l + 1)

        return longest


