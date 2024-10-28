class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])

        for r in range(row):
            if target <= matrix[r][col - 1]:
                left, right = 0, col - 1
                while left <= right:
                    mid = (left + right)//2
                    if matrix[r][mid] < target:
                        left = mid + 1
                    elif matrix[r][mid] > target:
                        right = mid - 1
                    else:
                        return True
                break

        return False