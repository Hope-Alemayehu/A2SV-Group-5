class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix = [1]
        postfix = [1] * (N + 1)

        for i in range(len(nums)-1):
            prefix.append(prefix[-1] * nums[i])

        for i in range(N - 1, 0, -1):
            postfix[i] = nums[i] * postfix[i+1]
        # print(postfix)
        for i in range (N - 1):
            prefix[i] *= postfix[i+1]
        
        return prefix


