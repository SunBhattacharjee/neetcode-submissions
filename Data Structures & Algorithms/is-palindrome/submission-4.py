class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()
        chars = "abcdefghifklmnopqrstuvwxyz0123456789"
        while l < r:
            if s[l] not in chars:
                l += 1
                continue
            if s[r] not in chars:
                r -= 1
                continue
            if not s[l] == s[r]:
                return False
            l += 1
            r -= 1

        return True