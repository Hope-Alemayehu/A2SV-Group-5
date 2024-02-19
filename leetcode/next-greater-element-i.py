class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapi = {}
        n = len(nums2)

        for i in range(n):
            j = i
            while j < n :
                if nums2[j] > nums2[i]:
                    mapi[nums2[i]] = nums2[j] 
                    break
                elif j == n - 1 and nums2[j] < nums2[i]:
                    mapi[nums2[i]] = - 1
                    break
                elif i == n -1:
                    mapi[nums2[i]] = - 1
                    break
                j += 1
        res = []
        for num in nums1:
            res.append(mapi[num])
        return res
