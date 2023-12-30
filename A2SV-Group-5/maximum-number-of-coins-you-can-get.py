class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        #time complexity O(NlogN)
        #space complexity O(1)
        piles.sort()
        t = len(piles) // 3
        myCoin = len(piles) - 2
        ans = 0

        while t:
            ans+= piles[myCoin]
            myCoin -= 2
            t-=1
        return ans
        
        