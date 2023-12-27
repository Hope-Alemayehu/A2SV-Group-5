class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        #time complexity O(NLogN)
        #space complexity O(1)
        points.sort()
        
        maxi = float("-inf")

        for i in range(len(points)-1):
            x1,y1=points[i]
            x2,y2=points[i+1]
            temp = x2-x1
            maxi = max(maxi,temp)
        return maxi