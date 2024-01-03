class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #time complexity O(N)
        #space complexity O(1)
        seek , p =0, 0

        while seek <len(nums):
            if nums[seek] !=0:
                nums[p] ,nums[seek] =nums[seek], nums[p]
                p += 1
            seek += 1
        return nums