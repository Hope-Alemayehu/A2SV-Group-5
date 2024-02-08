class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        total = 0
        res = 0
        for i in range (len(nums)):
            total += nums[i]
            q = total % k

            if q in prefix:
                res += prefix[q]
            prefix[q] = 1 + prefix.get(q,0)
        return res