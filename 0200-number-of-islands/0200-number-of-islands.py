class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #define the four directions
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        rows, cols = len(grid), len(grid[0])
        #define a dfs function
        def dfs(r: int,c: int) -> None:
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] != "1":
                return
          
            grid[r][c] = "2"

            for x, y in directions:
                nx, ny = r + x, c + y
                dfs(nx,ny)

        result = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    result += 1
                    dfs(i,j)
        return result

        #keep a global variable that counts the island
        #return that variable
