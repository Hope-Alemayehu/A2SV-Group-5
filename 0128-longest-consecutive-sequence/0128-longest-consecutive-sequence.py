class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0


        for num in nums:
            if num - 1 not in numSet:
                #to find the start of the array
                length = 0
                while num + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
        
        
        