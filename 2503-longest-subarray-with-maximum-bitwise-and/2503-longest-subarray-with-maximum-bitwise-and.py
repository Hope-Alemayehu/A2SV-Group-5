class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 1

        left = 0
        target = max(nums)


        for right in range(len(nums)):
            while left <= right and  nums[right] != target:
                ans = max(ans, right- left)
                left += 1
            
            ans = max(ans, right- left + 1)
            
        return ans