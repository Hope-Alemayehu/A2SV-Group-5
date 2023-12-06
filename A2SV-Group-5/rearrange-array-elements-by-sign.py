class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive=[]
        negative=[]
        res=[]
        n=len(nums)
        for i in range(n):
            if nums[i]<0:
                negative.append(nums[i])
            else:
                positive.append(nums[i])
        for i in range(n//2):
            res.append(positive[i])
            res.append(negative[i])
        return res