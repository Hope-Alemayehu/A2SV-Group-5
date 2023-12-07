class Solution:
    def printVertically(self, s: str) -> List[str]:
        words=s.split()
        max_length=max(len(word) for word in words)
        res=[]

        for i in range (max_length):
            curword=""
            for word in words:
                curword+=word[i] if i<len(word) else" "
            res.append(curword.rstrip())  #rstrip() is used to remove the trailing spaces
        return res



           