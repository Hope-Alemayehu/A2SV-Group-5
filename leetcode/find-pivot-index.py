class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]
        postfix = []
        total = sum(nums)

        for i in range(len(nums)):
            prefix.append(nums[i]+prefix[i])
            total -= nums[i]
            postfix.append(total)
        
        for i in range(len(nums)):
            if prefix[i] == postfix[i]:
                return i 
        return -1