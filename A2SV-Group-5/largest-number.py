class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if sum(nums) == 0:
            return "0"
        strList=[]

        for i in range(len(nums)):
            strList.append(str(nums[i]))
        
    
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if strList[i]+strList[j] > strList[j]+strList[i]:
                    continue
                else:
                    strList[i],strList[j] = strList[j],strList[i]
        
        ans = strList[::-1]
        return "".join(ans[::-1])