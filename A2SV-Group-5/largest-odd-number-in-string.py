class Solution:
    def largestOddNumber(self, num: str) -> str:
        while num:
            if int(num[-1])%2 !=0:
                return num
            else:
                num=num[:-1]
        return num