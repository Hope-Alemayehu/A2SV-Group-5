from functools import cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        @cache
        def dfs(alice, i, m):
            if i >= len(piles):
                return sum(piles[i:])
            
            res = 0 if alice else float("inf")
            for x in range(1, 2*m + 1):
                if i + x > len(piles):
                    break
                total = sum(piles[i:i+x])
                
                if alice:
                    res = max(res, total + dfs(not alice, i+x, max(m,x)))
                else:
                    res = min(res, dfs(not alice, i+x, max(m,x)))  

            return res

        return dfs(True, 0, 1)