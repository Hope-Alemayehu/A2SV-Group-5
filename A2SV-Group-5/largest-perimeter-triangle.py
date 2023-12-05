class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #sorted to maximize the value
       
        #if only there are three elements in the array
        #time complexity O(N)
        #space complexity O(1)
        
        nums.sort(reverse=True)  # Sort the array in descending order
        
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        
        return 0