class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        can=[False]*60
        for start,end in ranges:
            for x in range(start,end+1):
                can[x]=True
        for x in range(left,right+1):
            if not can[x]:
                return False
        return True


        