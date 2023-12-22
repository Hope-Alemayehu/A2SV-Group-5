class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        rows, cols = len(mat), len(mat[0])
        result = []
        r, c = 0, 0
        up = True

        while r < rows and c < cols:
            result.append(mat[r][c])

            # If the diagonal is going up
            if up:
                while r > 0 and c < cols - 1:
                    r -= 1
                    c += 1
                    result.append(mat[r][c])

                if c == cols - 1:
                    r += 1
                else:
                    c += 1
            # If the diagonal is going down
            else:
                while c > 0 and r < rows - 1:
                    r += 1
                    c -= 1
                    result.append(mat[r][c])

                if r == rows - 1:
                    c += 1
                else:
                    r += 1

            up = not up  # Toggle direction

        return result
