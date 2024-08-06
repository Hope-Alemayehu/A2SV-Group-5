class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
       
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):
            if r == rows or r < 0 or c == cols or c < 0 or grid[r][c] != "1":
                return
           
            grid[r][c] = -1
            for x, y in directions:
                rn = r + x
                cn = c + y
                dfs(rn,cn)
                
        ans = 0
        for i in range (rows):
            for j in range (cols):               
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i,j)                
        return ans

        





