class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        
        nums.sort()

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            hashi = set()
            for j in range(i+1, len(nums)):

                diff =  target - nums[j]
                if diff in hashi:
                    res.add(tuple([nums[i],nums[j],diff]))

                    while j+1 < len(nums) and nums[j] == nums[j+1]:
                        j += 1
                hashi.add(nums[j])
        return list(res)

