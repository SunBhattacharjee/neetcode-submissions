class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False

        s1 = {}
        s2 = {}

        for c in s:
            if not c in s1:
                s1[c] = 1
            else:
                s1[c] += 1

        for d in t:
            if not d in s2:
                s2[d] = 1
            else:
                s2[d] += 1
        
        for x in set(s):
            if not x in s1 or not x in s2 or not s1[x] == s2[x]:
                return False

        return True