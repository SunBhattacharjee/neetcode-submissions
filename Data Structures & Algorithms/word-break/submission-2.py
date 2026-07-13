class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True
        for i in range(n-1, -1, -1):
            for w in wordDict:
                wendsat = i + len(w)
                if wendsat <= n and s[i: wendsat] == w:
                    dp[i] = dp[wendsat]
                if dp[i]:
                    break
        return dp[0]
