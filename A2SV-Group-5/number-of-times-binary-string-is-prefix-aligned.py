class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxi=0
        count=0
        for i in range(len(flips)):
            if flips[i]>maxi:
                maxi=flips[i]
            if maxi==i+1:
                count+=1
        return count