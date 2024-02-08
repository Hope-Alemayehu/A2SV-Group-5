class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        total = 0
        prefixmap = {0:1}

        for i in range(len(nums)):
            total += nums[i]
            diff = total - k
            if diff in prefixmap:
                res += prefixmap[diff]
            prefixmap[total] = 1 + prefixmap.get(total,0)
        return res