class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "":
            return ""
        window, tcount = {}, {}
        for c in t:
            tcount[c] = tcount.get(c, 0) + 1

        found, need = 0, len(tcount)
        l = 0
        result, resultLength = [-1, -1], float("infinity")

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in tcount and window[c] == tcount[c]:
                found += 1
            
            while found == need:
                window[s[l]] -= 1
                if s[l] in tcount and window[s[l]] < tcount[s[l]]:
                    found -= 1
                if (r - l + 1) < resultLength:
                    result = [l, r]
                    resultLength = r - l + 1
                l += 1

        l, r = result
        return s[l: r + 1] if resultLength == float("infinity") else ""

