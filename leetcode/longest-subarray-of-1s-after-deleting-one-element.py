class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        if nums.count(1) == len(nums):
            return len(nums) - 1
        count = 0
        res = 0
        left = 0
        k = 1
        
        for r in range(len(nums)):
            if nums[r] == 1:
                count += 1
            else:
                k -= 1
            
            while k < 0:
                if nums[left] == 1:
                    count -= 1
                elif nums[left] == 0:
                    k += 1
                left += 1
            res = max(res,count)
      
        return res
