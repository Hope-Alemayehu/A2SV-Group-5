class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        near = float("inf")
        nums.sort()
        
        for i in range(len(nums)):
            cur = nums[i]
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                sume = cur + nums[left] + nums[right]
                
                if abs(target - sume) < near:
                    near = abs(target - sume)
                    res = sume
                
                if sume < target:
                    left += 1
                elif sume > target:
                    right -= 1
                else:
                    return res  # If sume equals target, no need to continue searching
                    
        return res
