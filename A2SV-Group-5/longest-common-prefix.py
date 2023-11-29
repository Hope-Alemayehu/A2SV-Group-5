class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #time complexity O(n^2)
        #space complexity O(K) k is the minimum length of the a string in the array
        x=""
        for i in range (len(strs[0])):
            for s in strs:
                if i==len(s) or s[i]!=strs[0][i]:
                    return x
            x+=strs[0][i]
        return x



           
                