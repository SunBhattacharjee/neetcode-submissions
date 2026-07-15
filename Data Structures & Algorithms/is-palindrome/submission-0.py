class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        r = len(s) - 1
        for l in range(len(s) - 1):
            if s[l] in chars and s[r] in chars:
                if not s[l] == s[r]:
                    return False
                r -= 1
        return True
