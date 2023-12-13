class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res=[]
        #checking membership in set is o(1) operartion
        #
        sp=set(spaces)
        for i ,c in enumerate(s):
            if i in sp:
                res.append(" ")
            res.append(c)
        return "".join(res)