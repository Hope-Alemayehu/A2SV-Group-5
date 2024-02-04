class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        #time complexity O(N)
        #space complexity O(N)
        prefix = [0]
        summ = 0

        for num in nums:
            if num == 1:
                summ += 1
            prefix.append(summ)
        freq = defaultdict(int)
        res = 0
        for val in prefix:
            if val - goal in freq:
                res += freq[val - goal]
            freq[val] += 1
        return res