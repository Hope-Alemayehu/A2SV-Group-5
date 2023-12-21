class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
       
        s=int("".join(map(str,digits)))+1
        res=[]
        s=str(s)
        for c in s:
            res.append(int(c))

        return res
        

