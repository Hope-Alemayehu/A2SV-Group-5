class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        res = [[rStart,cStart]]
        direction_index = 0
        r, c = rStart, cStart
        visited = {(rStart, cStart)}

        steps = 1
        while len(res) < rows * cols:
            for _ in range(2):
                for _ in range(steps):
                    dr, dc = directions[direction_index]
                    r, c = r + dr, c + dc
                    if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited:
                        res.append([r,c])
                        visited.add((r, c))
                direction_index = (direction_index + 1) % 4
            steps += 1

        return res