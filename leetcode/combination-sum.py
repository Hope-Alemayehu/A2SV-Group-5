class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(index,path):
            if sum(path) == target:
                ans.append(path.copy())
                return
            for j in range(index ,len(nums)):
                if sum(path)> target:
                    return
                else:
                    path.append(nums[j])
                    dfs(j,path)
                    path.pop()
       # nums.sort()
        dfs(0,[])
        return ans