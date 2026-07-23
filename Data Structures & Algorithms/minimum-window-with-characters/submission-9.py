class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "":
            return ""
        window, tcount = {}, {}
        for c in t:
            tcount[c] = 1 + tcount.get(c, 0)
        
        have, need = 0, len(tcount)
        l = 0
        res, resLen = [-1,-1], float("infinity")

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in tcount and window[c] == tcount[c]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in tcount and window[s[l]] < tcount[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if not resLen == float("infinity") else ""