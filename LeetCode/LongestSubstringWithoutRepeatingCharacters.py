class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set()
        left=0
        res=0
        for r in range (len(s)):
            while s[r] in charSet:
                charSet.remove(s[left])
                left+=1
            charSet.add(s[r])
            #r-left+1 is to calculate the length of the current substring
            res=max(res,r-left+1)
        return res