class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        count = 0
        left = 0

        for r in range(len(nums)):
            
            if nums[r] == 0:
                k -= 1
            
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            res = max(res , r - left + 1)
        return res