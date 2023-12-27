class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedn=sorted(nums)
        res=[]
        for i in range(len(nums)):
            res.append(sortedn.index(nums[i]))
        return res