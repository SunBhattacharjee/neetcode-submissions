class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        ls = s.lower()
        l = 0
        r = len(s) - 1

        while (l < r):
            if ls[l] not in chars:
                l += 1
                continue
            if ls[r] not in chars:
                r -= 1
                continue
            if not ls[l] == ls[r]:
                return False
                
            l += 1
            r -= 1
        
        return True
