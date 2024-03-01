class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        maxi = nums[0]
        prefix = nums[0]

        for idx in range(1, len(nums)):
            curr = nums[idx]
            prefix += curr

            if curr > maxi:
                maxi = max(maxi, math.ceil(prefix / (idx + 1)))

        return maxi