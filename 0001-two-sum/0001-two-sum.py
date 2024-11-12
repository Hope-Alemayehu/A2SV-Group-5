class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a hash map -> key: number and the value: index
        indexMap = defaultdict(int)
        #iterate through the list
        N = len(nums)
        for i in range(N):
            #check if [target - num[i]] in the hash map
            reminder = target - nums[i]
            if reminder in indexMap:
                #if yes return the indices of those numbers
                return [indexMap[reminder], i]
            #insert nums[i] to the map
            indexMap[nums[i]] = i
    
        
        