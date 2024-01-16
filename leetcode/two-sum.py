class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashi = {}

        for i, n in enumerate(nums):

            diff = target - n
            if diff in hashi:
                return [hashi[diff],i]
            hashi[n] = i
        return 