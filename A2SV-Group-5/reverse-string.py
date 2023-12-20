class Solution:
    def reverseString(self, s: List[str]) -> None:
        # left = 0
        # right = len(s) - 1
        # while left < right:
        #     s[left], s[right] = s[right], s[left]
        #     left += 1
        #     right -= 1
        # return s
        self.reverseHelper(s,0,len(s)-1)
    def reverseHelper(self,s:List[str],left:int,right:int):
        if left>=right:
            return s
        
        s[left],s[right]=s[right],s[left]
        self.reverseHelper(s,left+1,right-1)