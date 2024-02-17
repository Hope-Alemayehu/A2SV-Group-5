class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0

        count = Counter(s)
        res = 0
        hasOdd = False

        for val in count.values():
           
            if val % 2 == 0:
                res += val
            else:
                res += (val - 1)
                hasOdd = True
        if hasOdd:
            res += 1
            
        return res