class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #this doesn't work because we have negative numbers and 
        #we can't do a sliding window with negative numbers inside
        prefix = [0]
        hashi = defaultdict(int)
        for i in range(len(nums)):
            prefix.append(nums[i] + prefix[i])
            
        result = 0
        
        for val in prefix:
            if (val - k) in hashi:
                result += hashi[val - k]
            hashi[val] += 1
     
        return result