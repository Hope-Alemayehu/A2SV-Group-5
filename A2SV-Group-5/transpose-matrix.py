class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Complexity Analysis
		# time complexity O(N^2)
		# space complexity O(row*col) 
        
        row=len(matrix)
        col=len(matrix[0])
        
        transpose=[[0]*row for _ in range(col)]
        
        for r in range(row):
            for c in range(col):
                transpose[c][r]=matrix[r][c]
        return transpose
