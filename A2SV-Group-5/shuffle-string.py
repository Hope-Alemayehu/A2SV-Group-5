class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        #give a string s and integer array
        #shuffle the strings using yhe indices array
        n=len(indices)
        res=[0]*n
        
        for i in range(n):
            res[indices[i]]=(s[i])
            
        return "".join(res)