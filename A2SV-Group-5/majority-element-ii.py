class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #time complexity O(N)
        #space complexity O(N)
        
        #appearance 
        appear=len(nums)//3

        #to count the occurence of each integer in array
        counted=Counter(nums)
        res=[]
        for c in counted:
            if counted[c]>appear:
                res.append(c)
        return res