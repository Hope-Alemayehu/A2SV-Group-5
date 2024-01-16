class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(nums) == 1:
            return len(nums)
        
        left , right = 0 ,1
        
        while right < len(nums):
            if nums[left] == nums[right]:
                
                while right < len(nums) and nums[left] == nums[right]:
                    right += 1
                if right < len(nums):
                    left += 1
                    nums[left] = nums[right]
            else:
                left += 1
                right += 1
        return left+1