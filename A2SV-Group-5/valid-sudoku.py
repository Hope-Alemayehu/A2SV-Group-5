class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rowstart rs
        #rowend re
        #columnstart cs
        #columnend ce
        def checkboxes( rs,re,cs,ce,board):
            checkset=set()
            for i in range(rs,re+1):
                for j in range(cs,ce+1):
                    if board[i][j] !="." and board[i][j] in checkset:
                        return False
                    if board[i][j] !=".": 
                        checkset.add(board[i][j])
            return True

        #to check if each rows are valid
        def checkrows(r,board):
            checkrowset=set()
            for i in range(9):
                if board[r][i] in checkrowset:
                    return False
                if board[r][i] !=".": 
                    checkrowset.add(board[r][i])
            return True

        #to check if each cols are valid
        def checkcols(c,board):
            checkcolset=set()
            for i in range(9):
                if board[i][c] in checkcolset:
                    return False
                if board[i][c] !=".": 
                    checkcolset.add(board[i][c])
            return True
        
        for i in range(9):
            if not checkrows(i,board) or not checkcols(i,board):
                return False
            
            
        if not checkboxes(0, 2, 0, 2, board) or not checkboxes(0, 2, 3, 5, board) or not checkboxes(0, 2, 6, 8, board) \
                or not checkboxes(3, 5, 0, 2, board) or not checkboxes(3, 5, 3, 5, board) or not checkboxes(3, 5, 6, 8, board) \
                or not checkboxes(6, 8, 0, 2, board) or not checkboxes(6, 8, 3, 5, board) or not checkboxes(6, 8, 6, 8, board):
            return False

        return True

        