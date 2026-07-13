class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(gird, r, c, visit):
            ROWS, COLS= len(grid), len(grid[0])
            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == 1:
                return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            visit.add((r, c))
            ways = 0
            ways += dfs(grid, r, c + 1, visit)
            ways += dfs(grid, r + 1, c, visit)
            ways += dfs(grid, r, c - 1, visit)
            ways += dfs(grid, r - 1, c, visit)

            visit.remove((r, c))
            return ways

        return dfs(grid, 0, 0, set())

        