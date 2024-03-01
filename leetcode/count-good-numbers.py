class Solution:
    def countGoodNumbers(self, n: int) -> int:
        Mod = 1000000007
        odd = n // 2
        even = n - odd
    
        if even == 1 and odd == 0:
            return 5
        
        def calc(x,n):
            if n == 0:
                return 1
            if n%2 == 0:
                return calc((x*x)%Mod,n//2)
            else:
                return x * calc((x*x)%Mod,n//2)
        
        oddT = 4
        evenT = 5
        res = 1
        res *= calc(evenT,even)
        res *= calc(oddT,odd)

        return res % Mod
        