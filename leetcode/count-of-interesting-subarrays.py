class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefix = [0]
        count = 0
        for i in range(len(nums)):
            if nums[i] % modulo == k:
                count += 1
            prefix.append(count)
        
        freq = defaultdict(int)
        res = 0

        for val in prefix:
            res += freq[(val + modulo - k) % modulo]
            freq[val % modulo] += 1
        return res