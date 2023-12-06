class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # Time complexity=O(N)
        # space complesxity O(N)
        left=0
        right=n
        res=[]
        while left<right and right<len(nums):
            res.append(nums[left])
            left+=1
            res.append(nums[right])
            right+=1
        return res