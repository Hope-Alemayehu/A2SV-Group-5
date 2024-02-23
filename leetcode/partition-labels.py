class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #time complexity O(N)
        #space complexity O(26) which is gonna be O(1)
        
        indexMap = {}

        for i , c in enumerate(s):
            indexMap[c] = i
        
        res = []
        end = 0 
        size = 0

        for i in range(len(s)):
            size += 1
            end = max(end,indexMap[s[i]])

            if i == end:
                res.append(size)
                size = 0
        return res