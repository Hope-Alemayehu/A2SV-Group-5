class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=len(matrix)
        cols=len(matrix[0])
        # check=set()
        for r in range (rows):
            for c in range (r,cols):
                if r==c:
                    continue
                # if (r,c) not in check:
                matrix[r][c],matrix[c][r]=matrix[c][r],matrix[r][c]
                # check.add((r,c))
                # check.add((c,r))
        for row in matrix:
            row.reverse()
        return matrix