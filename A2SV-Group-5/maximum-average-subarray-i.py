class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        

        #prepare the window
        sum = 0
        for i in range(k):
            sum += nums[i]
        maxi = sum/k
        left = 0
        for i in range(k,len(nums)):
            sum -= nums[left]
            sum += nums[i]
           
            maxi = max(maxi , sum/k)
            left += 1
          
        return maxi