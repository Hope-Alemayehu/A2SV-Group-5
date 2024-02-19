class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss , i , patch = 1,0,0
    
        while miss <= n:

            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss *= 2
                patch += 1
        return patch