class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        def dfs(r: int, c: int, heap:List[List[int]]) -> list:
            if r < 0 or r >= rows or c < 0 or c >= cols or land[r][c] == 0:
                return 
            if land[r][c] == 2:
                return 
            land[r][c] = 2
            heapq.heappush(heap,[-r,-c])
            for x, y in directions:
                dfs(r + x, c + y,heap)
        
            return heap[0]

        #get the dimention of the land
        rows, cols = len(land), len(land[0])
        #create a list for the result
        result = []
        #directions (left, right,up, down)
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        #we iterate throught the land
        for r in range(rows):
            for c in range(cols):

                #we check if its a farmland
                if land[r][c] == 1:
                    #create temporary list
                    #add the starting cell and call the dfs function
                    heap = []
                    temp = [r,c]
                    res = dfs(r,c,heap)
                    temp = temp + [abs(res[0]), abs(res[1])]
                    result.append(temp)
        return result
    
