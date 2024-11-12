class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        #define the basic dfs function
        def dfs(r: int, c:int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return 
            visited.add((r,c))

            for x, y in directions:
                nx, ny = x + r, y + c
                if (nx,ny) not in visited:
                    dfs(nx, ny)
                    
        #get the dimentions of the grid
        rows, cols = len(grid), len(grid[0])
        #create a visited set
        visited = set()
        #create a list of the possible directions
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        #create a variable to store the result
        result = 0 
        #iterate over each cells
        for r in range(rows):
            for c in range(cols):
                #if the cell isn't in the visited set and has value of "1" call dfs
                if (r,c) not in visited and grid[r][c] == "1":
                    result += 1
                    dfs(r,c)
        return result

        
            
