class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        #time complexity O(log n)
        #space complexity O(1)
        while n>0:
            d=n%3
            if d==2:
                return False
            n//=3
        return True