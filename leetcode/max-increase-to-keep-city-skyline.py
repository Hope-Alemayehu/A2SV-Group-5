class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        N = len(grid)
        rows = [0] * N

        #cols[i] is the highest of column i
        cols = [0] * N

        #trying to get the highest of the columns and rows
        for x in range(N):
            for y in range(N):
                rows[x] = max(rows[x],grid[x][y])
                cols[y] = max(cols[y],grid[x][y])
        total = 0

        for x in range(N):
            for y in range(N):
                total += max(min(rows[x],cols[y]) - grid[x][y],0)
        return total