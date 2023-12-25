class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans=0
        
        n=len(mat)
        for i in range (len(mat)):
            for j in range(len(mat[0])):
                if i==j:
                    ans+=mat[i][j]
                elif i+j == n-1 :
                    ans+=mat[i][j]
       
        
        return ans
            
    

            