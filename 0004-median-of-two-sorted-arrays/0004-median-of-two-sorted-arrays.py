class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = []

        up, down = 0, 0
        while up < len(nums1) and down < (len(nums2)):
            if nums1[up] <= nums2[down]:
                total.append(nums1[up])
                up += 1
            else:
                total.append(nums2[down])
                down += 1
        total.extend(nums1[up:])
        total.extend(nums2[down:])
        # print(total)
        mid = len(total)//2
        if  len(total) % 2:
            return float(total[mid])
        else:
            summ = total[mid-1] + total[mid]
            return summ/2

        return 0
