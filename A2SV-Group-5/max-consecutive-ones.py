class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums)==1 and nums[0]==0:
            return 0
        if len(nums)==1 and nums[0]==1:
            return 1
        
        longest=0
        l=0
        
        for r ,n in enumerate(nums):
            if n==0:
                l=r+1
            longest=max(longest,r-l+1)
        return longest

