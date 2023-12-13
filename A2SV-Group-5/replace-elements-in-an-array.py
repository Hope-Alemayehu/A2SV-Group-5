class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hashi={}
        for i in range(len(nums)):
            hashi[nums[i]]=i
        
        for num,change in operations :
            idx = hashi[num]
            nums[idx]=change
            hashi.pop(num)
            hashi[change]=idx

        return nums
