class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #time complexity O(N)
        #space complexity O(N)
        res=[]
        large=max(candies)
        
        for i in range(len(candies)):
            cur= candies[i]+ extraCandies
            if cur >= large:
                res.append(True)
            else:
                res.append(False)
        return res