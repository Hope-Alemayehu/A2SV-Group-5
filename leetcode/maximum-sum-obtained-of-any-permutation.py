class Solution:
    def maxSumRangeQuery(self, nums: List[int], req: List[List[int]]) -> int:
        n = len(nums)
        r = len(req)
        a = [0] * n  # freq list
        
        for i in range(r):
            a[req[i][0]] += 1
            if req[i][1] < n - 1:
                a[req[i][1] + 1] -= 1
        
        for i in range(1, n):
            a[i] += a[i - 1]

        a.sort()
        nums.sort()
        
        ans = 0
        MOD = int(1e9) + 7
        
        for i in range(n - 1, -1, -1):
            ans += (a[i] * nums[i]) % MOD
            ans %= MOD
        
        return ans
