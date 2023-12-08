class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)+1
        summ=sum(i for i in range(n))
        actualSum=sum(nums)
        return summ-actualSum
        