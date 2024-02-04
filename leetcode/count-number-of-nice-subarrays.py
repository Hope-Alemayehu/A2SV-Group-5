class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        oddc = 0
        prefix = [0]

        for num in nums:
            oddc += num % 2
            prefix.append(oddc)
        
        freq = defaultdict(int)
        res = 0
        for val in prefix:
            if val - k in freq:
                res += freq[val - k]
            freq[val] += 1
        return res