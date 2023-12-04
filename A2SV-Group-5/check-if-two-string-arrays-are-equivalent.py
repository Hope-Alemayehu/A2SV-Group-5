class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        #time complexity O(m+n)  m be the the size of word1 and n be the size  of word2
        #space complexity O(m+n)

        s="".join(word1)
        t="".join(word2)
        return s==t