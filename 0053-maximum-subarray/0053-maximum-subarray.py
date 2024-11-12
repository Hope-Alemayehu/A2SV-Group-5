class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #time complexity O(N)
        #space complexity O(1)

        #initalize max_sum variable
        max_sum = nums[0]
        #initalize the cur_sum variable
        cur_sum = nums[0]
        #iterate the array
        for i in range(1,len(nums)):  
            #if cur_sum is below zero, reassign it to 0
            cur_sum = max(cur_sum + nums[i], nums[i])
            #maxize the max_sum 
            max_sum = max(cur_sum, max_sum)
        return max_sum 
