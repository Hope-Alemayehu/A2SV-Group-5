class Solution:
    def isHappy(self, n: int) -> bool:
        #time complexity= O(N)
        #space complexity= O(N)
        visit=set()
        while n not in visit:
            visit.add(n)
            n=self.sumSquare(n)

            if n==1:
                return True
        return False

    def sumSquare(self,n:int)->int:
        output=0
        while n:
            digit=n%10
            output+=(digit**2)
            n=n//10
        return output