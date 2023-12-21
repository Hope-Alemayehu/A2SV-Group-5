class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        #time complexity O(N^2)
        #space complexity O(1)

        pair=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and (i*j)%k==0:
                    pair+=1
            
        return pair

