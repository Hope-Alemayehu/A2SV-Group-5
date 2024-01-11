class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #time complexity O(N)
        #space complexity O(1)
        #approch: Sliding window
        
        shortest = float("inf")

        left = 0
        curSum = 0
        for r in range(len(nums)):
            curSum += nums[r]
            
            while curSum >= target:
                shortest = min(shortest, r-left+1)
                curSum -= nums[left]
                left += 1
        
        return shortest if shortest != float("inf") else 0