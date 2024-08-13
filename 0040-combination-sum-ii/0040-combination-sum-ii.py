class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        
        def dfs(index,path):
            if sum(path) == target:
                ans.append(path.copy())
                return
            for j in range(index,len(nums)):
                if sum(path) + nums[j] > target:
                    return
                #to avoid duplicates
                if j > index and nums[j] == nums[j-1]:
                    continue
                path.append(nums[j])
                dfs(j+1,path)
                path.pop()
            
        dfs(0,[])
        return ans
