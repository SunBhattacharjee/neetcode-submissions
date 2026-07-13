class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def f(i, j):
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1
            return f(i-1, j) + f(i, j-1)
        return f(m - 1, n - 1)

        