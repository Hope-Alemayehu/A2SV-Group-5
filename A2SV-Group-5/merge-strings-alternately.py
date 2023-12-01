class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #time complexity O(N) n= minimum length of word1 and word2
        #space complexity O(N)
        length=min(len(word1),len(word2))
        s=""
        for i in range(length):
            s+=word1[i]
            s+=word2[i]
        if length !=len(word1):
            s+=word1[length:]
        if length !=len(word2):
            s+=word2[length:]
        
        return s     