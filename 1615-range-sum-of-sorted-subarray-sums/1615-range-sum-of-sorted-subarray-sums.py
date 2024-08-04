class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarraySum = [] + nums
        N = len(nums)
        Mod = 10**9 + 7
        
        for i in range(N):
            cur = nums[i]
            for j in range(i+1,N):
                
                cur += nums[j]
                subarraySum.append(cur)
                
        subarraySum.sort()
        # print(subarraySum)
        ans = sum(subarraySum[left - 1 : right])
    
        return ans % Mod 

