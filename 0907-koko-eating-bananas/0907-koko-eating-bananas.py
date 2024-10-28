class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #time complexity O(nLogM) M is the maximum element in piles
        #space complexity O(1)
        def time(k):
            ans = 0
            for pile in piles:
                if pile <= k:
                    ans += 1
                else:
                    ans += (pile//k)
                    if pile % k:
                        ans += 1       
            return ans


        right = max(piles)
        left = 1

        while left < right:
            mid = (left + right)//2
            hour = time(mid)
            # print(hour)
            if hour <= h:
                right = mid
            else:
                left  = mid + 1
        return right

