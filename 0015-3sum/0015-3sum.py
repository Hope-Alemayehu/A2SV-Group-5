class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)

        for i in range(len(nums)):
            if i ==0 or (i != 0 and nums[i] != nums[i - 1]):

                left = i + 1
                right = n -1
                while left < right:
                    if nums[i] + nums[left] + nums[right] == 0:
                        res.add(tuple([nums[i], nums[left],nums[right]]))
                        left += 1
                        right -= 1
                    elif nums[i] + nums[left] + nums[right] > 0:
                        right -= 1
                    else:
                        left += 1
        return list(res)