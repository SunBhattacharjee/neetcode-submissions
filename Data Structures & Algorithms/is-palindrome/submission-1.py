class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        r = len(s) - 1
        lowerString = s.lower()
        for l in range(len(lowerString) - 1):
            if lowerString[l] in chars and lowerString[r] in chars:
                if not lowerString[l] == lowerString[r]:
                    return False
                r -= 1
        return True
