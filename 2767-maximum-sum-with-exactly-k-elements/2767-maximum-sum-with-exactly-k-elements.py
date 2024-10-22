class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maxi = max(nums)
        ans = 0

        for i in range(k):
            ans += maxi
            maxi += 1
        return ans