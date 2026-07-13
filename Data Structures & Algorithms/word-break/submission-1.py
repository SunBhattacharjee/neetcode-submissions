class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True
        for i in range(n-1, -1, -1):
            for w in wordDict:
                newLen = i + len(w)
                if newLen <= n and s[i: newLen] == w:
                    dp[i] = dp[newLen]
                if dp[i]:
                    break
        return dp[0]
