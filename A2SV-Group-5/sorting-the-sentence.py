class Solution:
    def sortSentence(self, s: str) -> str:
        #time complexity O(N)
        #space complexity O(N)
        splited = s.split()
        res=[0]*len(splited)
        for word in splited:
        
            val = int(word[-1]) - 1
            last = len(word)-1
            res[val]= word[:last]
        return " ".join(res)

        