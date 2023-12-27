class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #selection sort
        #time complexity O(N^2)
        #space complexity O(1)

        for i in range(len(nums)):
            curmin=i
            print(curmin)
            for j in range(i,len(nums)):
                if nums[j]<nums[curmin]:
                    curmin=j
                    
            nums[i],nums[curmin]=nums[curmin],nums[i]
        return nums
        