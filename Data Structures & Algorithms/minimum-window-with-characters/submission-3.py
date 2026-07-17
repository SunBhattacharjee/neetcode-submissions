class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "":
            return ""
        tcount, window = {}, {}
        # count t
        for c in t:
            tcount[c] = 1 + tcount.get(c, 0)

        need, found = len(tcount), 0
        res, resLen = [-1, -1], float("infinity")
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in tcount and window[c] == tcount[c]:
                found += 1

            while need == found:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in tcount and window[s[l]] < tcount[s[l]]:
                    found -= 1
                l += 1

        if resLen == float("infinity"):
            return ""
        else:
            return s[res[0]: res[1] + 1]
