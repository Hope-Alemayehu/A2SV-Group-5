class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s,p = 0,0

        while s < len(nums):
            if nums[s] !=0:
                nums[s], nums[p] = nums[p], nums[s]
                p +=1
            s += 1
            
            # if nums[s] == 0:
            #     s+=1
            # if nums[p] !=0:
            #     p+=1
            
        return nums


