class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        """
        rows, cols = len(matrix), len(matrix[0])

        rowS, colS = set(),set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rowS.add(r)
                    colS.add(c)

        for num in list(rowS):
            for c in range(cols):
                matrix[num][c] = 0 



        for num in list(colS):
            for r in range(rows):
                matrix[r][num] = 0
      