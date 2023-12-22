class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        small, middle = float('inf'), float('inf')

        for num in nums:
            if num <= small:
                small = num
            elif num <= middle:
                middle = num
            else:
                return True

        return False
