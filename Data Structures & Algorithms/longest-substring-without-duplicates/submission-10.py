class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = set()
        l = 0
        # pwwkew
        # p 0 0 {p} 1 1
        # w 0 1 {p,w} 2 2
        # w 1 2 {p} 1, 2
        # k 1 3 {p, k} 2, 2
        # e 1 4 {p, k, e} 3, 3
        
        for r in range(len(s)):
            c = s[r]
            while c in seen:
                seen.remove(s[l])
                l += 1
            length = r - l + 1
            longest = max(longest, length)
            seen.add(c)
        return longest

