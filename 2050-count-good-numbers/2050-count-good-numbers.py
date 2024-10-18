class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        result = 1
        def binary_exp(a,b):
            nonlocal result
            while b > 0:
                if b & 1:
                    result = (result % mod * a % mod) % mod 
                a = (a % mod * a % mod) % mod 
                b >>= 1
            return result % mod

       
        even = n // 2 + n % 2
        odd = n - even
        if even:
            (binary_exp(5, even))
        if odd:
            (binary_exp(4, odd))
        return (result) % mod