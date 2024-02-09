class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = []
        n = len(nums)
        sufix = [0] * n
        

        cur = 0
        for i in range (n):
            cur += nums[i]
            prefix.append(cur)
        

        #preparing sufix
        cur = 0
        for i in range (n-1,-1,-1):
            cur += nums[i]
            sufix[i] = cur
       
        res = [0]*n
        for i in range(n):
            res[i] = nums[i] * i - prefix[i] + sufix[i] - (nums[i]*(n-i-1))
        
        return res

            