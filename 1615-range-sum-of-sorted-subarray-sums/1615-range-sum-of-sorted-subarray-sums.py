import heapq

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        pq = []
        subarraySum = []
        N = len(nums)
        
        # Initialize priority queue with single-element subarrays
        for i in range(N):
            heapq.heappush(pq, (nums[i], i, i))
        
        # Generate subarray sums and store in priority queue
        for _ in range(right):
            val, start, end = heapq.heappop(pq)
            subarraySum.append(val)
            if end + 1 < N:
                heapq.heappush(pq, (val + nums[end + 1], start, end + 1))
        
        # Return the sum of the subarray sums from index left to right
        return sum(subarraySum[left - 1:right]) % MOD