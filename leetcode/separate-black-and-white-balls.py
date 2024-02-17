class Solution:
    def minimumSteps(self, s: str) -> int:
        #seeker and placeholder type of two pointers

        #seeker find the zero
        # pplace holder if the one that will hold the postion until we get the first zero
       

        se , p  = 0 , 0
        res = 0
        while p < len(s):
            while p < len(s) and s[p] == "1":
                p += 1
            if p < len(s) and s[p] == "0":
                
                res += p - se
                se += 1
            p += 1
        return res
            