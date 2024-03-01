from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        if total % p == 0:
            return 0
        target_rem = total % p

        prefix_rem = 0
        right_rem = {0: -1}  # Store prefix remainders and their corresponding indices
        
        res = len(nums)
        current_rem = 0
        
        for i, num in enumerate(nums):
            prefix_rem = (prefix_rem + num) % p
            current_rem = (prefix_rem - target_rem) % p

            if current_rem in right_rem:
                j = right_rem[current_rem]
                res = min(res, i - j)
            right_rem[prefix_rem] = i  # Update the right most remainder index
        
        return res if res < len(nums) else -1
