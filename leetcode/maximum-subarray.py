class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #time complexity O(N)
        #space complexity O(1)
        max_value_so_far = float("-inf")
        cur_max = 0

        for i in range(len(nums)):
            cur_max += nums[i]
            
            if max_value_so_far < cur_max:
                max_value_so_far = cur_max
            if cur_max < 0:
                cur_max = 0
        return max_value_so_far
                