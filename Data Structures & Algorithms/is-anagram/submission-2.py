class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = set(s)
        s2 = set(t)

        if not len(s) == len(t):
            return False
        
        for c in s1:
            if not c in s2:
                return False

        return True