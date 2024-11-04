class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_Average = 0
        summ = 0

        for i in range(k):
            summ += nums[i]

        max_Average = summ / k
        left = 0

        for i in range(k, len(nums)):
            summ -= nums[left]
            left += 1
            summ += nums[i]
            max_Average = max(max_Average, summ / k)
            
        return max_Average
