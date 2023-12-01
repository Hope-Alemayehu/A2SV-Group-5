from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def isDiagonal(row: int, col: int) -> bool:
            value = matrix[row][col]
            while row < len(matrix) and col < len(matrix[0]):
                if value != matrix[row][col]:
                    return False
                row += 1
                col += 1
            return True  # Add this line

        for col in range(len(matrix[0])):
            if not isDiagonal(0, col):
                return False
        for row in range(1, len(matrix)):
            if not isDiagonal(row, 0):
                return False
        return True
