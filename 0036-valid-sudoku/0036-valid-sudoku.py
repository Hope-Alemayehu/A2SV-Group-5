class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkColumn(j):
            check = set()
            for r in range (9):
                if board[r][j].isnumeric() and board[r][j] in check:
                    return False
                check.add(board[r][j])
            return True
                

        def checkRow(i):
            check = set()
            for c in range (9):
                if board[i][c].isnumeric() and board[i][c] in check:
                    return False
                check.add(board[i][c])
            return True

        #0, 2, 6
        def matrices(r,c):
            seen = set()
            for i in range (3):
                for j in range(3):
                    num = board[r+i][c+j]
                    if num.isnumeric() and num in seen:
                        return False
                    seen.add(num)
            return True
        
        three = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
        for i in range(9):
            if not checkRow(i):
                return False
            
            if not checkColumn(i):
                return False
        
        for r,c in three:
            flag = matrices(r,c)
            if not flag:
                return False
        return True
        
