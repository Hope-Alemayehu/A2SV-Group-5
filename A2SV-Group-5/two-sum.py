class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap={}

        for i ,n in enumerate(nums):
            diff=target-n
            if diff in nummap:
                return [nummap[diff],i]
            nummap[n]=i
        return