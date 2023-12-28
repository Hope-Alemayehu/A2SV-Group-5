class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1set=set(nums1)
        num2set=set(nums2)
        
        res=[]
        for i in range(len(nums1)):
            if nums1[i] in num1set and nums1[i] in num2set and nums1[i] not in res: 
                    count= min(nums1.count(nums1[i]) , nums2.count(nums1[i]))
                    res.append(nums1[i])
                    while count >1:
                        res.append(nums1[i])
                        count-=1
        return res