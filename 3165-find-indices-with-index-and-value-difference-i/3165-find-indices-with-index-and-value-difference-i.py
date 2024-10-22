class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        #time complexity O(N^2)
        #space complexity O(1)
        n = len(nums)
        for i in range(0,n - indexDifference):
            for j in range(i, n):
                if abs(i - j ) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i,j]
        return [-1, -1]