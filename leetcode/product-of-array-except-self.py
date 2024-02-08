class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]
        postfix = [1]*n
        
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1] * nums[i-1])
        

        for i in range(n-1,-1,-1):
            if i == n-1:
                postfix[n-1] = 1
            else:
                postfix[i] = nums[i+1] * postfix[i+1]

        for i in range (n):
            prefix[i] = prefix[i] * postfix[i]
        return prefix
