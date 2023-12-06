class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        #time complexity O(N)
        #space complexity O(1)
        step=0
        for i in range(len(points)-1):
            step+=max(abs(points[i][0]-points[i+1][0]),abs(points[i][1]-points[i+1][1]))
        return step