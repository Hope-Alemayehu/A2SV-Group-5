class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        stack = []
        res = 0
        def dfs(r,c):
            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] != 1:
                return 0
            
            grid[r][c] = -1
            count = 1
            for x, y in directions:
                rn, cn = r + x, c + y
                count += dfs(rn,cn)
            return count
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, dfs(r,c))
        return res

