class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        #time complexity O(N)
        #space complexity O(1)
        up = 0
        down = 0
        
        # n = min (len(nums1),len(nums2))
        # for i in range(n):
        #     if nums1[up]<nums2[down]:
        #         up += 1
        #     elif nums1[up] > nums2[down]:
        #         down += 1
        #     else:
        #         return nums1[up]
        # return -1

        while up < len(nums1) and down < len(nums2):

            if nums1[up] > nums2[down]:
                down += 1
            elif nums1[up] < nums2[down]:
                up += 1
            else:
                return nums1[up]
        return  -1