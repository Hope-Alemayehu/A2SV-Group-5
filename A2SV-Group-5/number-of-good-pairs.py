class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        #time complexity O(N^2)
        #space complexity O(1)
        #lets do the brute force first
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    count+=1
        return count