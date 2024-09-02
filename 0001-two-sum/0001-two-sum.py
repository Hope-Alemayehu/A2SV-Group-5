class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}
        for i, num in enumerate (nums):
            if target - num in counter:
                index = counter[target - num]
                return [index,i]
                break
            counter[num] = i
       
