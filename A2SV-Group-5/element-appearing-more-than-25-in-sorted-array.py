class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        times=0.25 * len(arr)
        timescounter=Counter(arr)
      
        for key,value in timescounter.items():
            if value>times:
                return key
        