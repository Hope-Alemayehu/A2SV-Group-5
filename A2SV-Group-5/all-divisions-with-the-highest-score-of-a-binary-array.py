class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones=nums.count(1)
        zeros=nums.count(0)

        score=[ones]
        curzero=0
        for i in range(1,len(nums)+1):
            if nums[i-1]==0:
                curzero+=1
            else:
                ones-=1
            score.append(curzero+ones)
        ans=[]
        maxi=max(score)
        for i in range(len(score)):
            if score[i]==maxi:
                ans.append(i)
        return ans