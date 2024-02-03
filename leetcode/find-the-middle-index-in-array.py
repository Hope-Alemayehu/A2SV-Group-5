class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = [0]
        postfix = []
        total = sum(nums)

        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
            else:
                cur = nums[i] + prefix[i]
                prefix.append(cur)
            total -= nums[i]
            postfix.append(total)
        
        for i in range(len(nums)):
            if prefix[i] == postfix[i]:
                return i
        return -1