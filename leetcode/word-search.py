class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #get the dimention
        row = len(board)
        col = len(board[0])
        path = set()

        #i indicate the current index for the chrarcter in the word
        def dfs(r,c,i):
            #meaning we have found all the character for the word
            if i == len(word):
                return True
            #conditions not to go further
                #if we are out of bound 
                #if the current character in the matrix don't match with word[i]
                #if we have visited that node before
            if (r<0 or c<0 or r>= row or c >= col
                or board[r][c] != word[i] or (r,c) in path):
                return False
            path.add((r,c))
            #to check all the possible direction
            if dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1):
                return True
            path.remove((r,c))

        for r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        return False