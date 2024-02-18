class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #time complexity O(NlogN)
        #space complexity O(1)
        if not points:
            return 0
        
        points.sort(key = lambda x :x[1])
        arrow = 1
        end = points[0][1]  #to start compare 

        for start,newend in points[1:]:
            if start > end: #there is no intersection
                arrow += 1     #there is more arrow needed in this case
                end = newend
        return arrow