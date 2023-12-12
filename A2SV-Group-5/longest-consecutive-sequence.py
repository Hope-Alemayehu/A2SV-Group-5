from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        count = 1  # Initialize count to 1, as a single element is always a consecutive sequence.
        max_count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements

            if nums[i] == nums[i - 1] + 1:
                count += 1
            else:
                count = 1  # Reset count for non-consecutive elements

            max_count = max(max_count, count)

        return max_count

