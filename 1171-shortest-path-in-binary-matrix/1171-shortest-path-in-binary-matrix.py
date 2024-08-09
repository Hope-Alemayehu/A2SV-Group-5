class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #to get the shortest path we van make sure to use BFS
        
        def inbound(r,c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0:
                return True

            return False

        queue = deque()
        queue.append([0,0,1])

        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        rows, cols = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[rows-1][cols-1] ==1:
            return -1
        if rows == 1 and cols == 1 and grid[0][0] == 0:
            return 1
        
        grid[0][0] = 1
        while queue:
            r, c ,level = queue.popleft()

            for x, y in directions:
                rn, cn = r+ x, y+c
                if inbound(rn, cn) :
                    if rn == rows - 1 and cn == cols -1:
                        return level + 1
                    queue.append([rn,cn,level+1])
                    grid[rn][cn] = 1
            
        return -1
        
            
                    

            
