class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case for empty string
        if s == "":
            return ""
        # populating tcount
        tcount = {}
        for c in t:
            tcount[c] = 1 + tcount.get(c, 0)

        # have & need + variable dec
        have, need = 0, len(tcount)
        window = {}
        res, resLen = [-1,-1], float("infinity");
        l = 0

        # main loop
        for r in range(len(s)):
            c = s[r]
            # add to window {}
            window[c] = 1 + window.get(c, 0)

            # march freq and update have
            if c in tcount and tcount[c] == window[c]:
                have += 1

            # when condition is met, update & shrink
            while have == need:
                # update values & wanting minimum
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # shrink window + update window freqs
                window[s[l]] -= 1
                if s[l] in tcount and window[s[l]] < tcount[s[l]]:
                    have -= 1
                l += 1
                
        l, r = res
        if resLen != float("infinity"):
            return s[l:r+1]
        else:
            return ""


        