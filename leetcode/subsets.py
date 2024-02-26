class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(i,path,l):
            nonlocal ans
            #the length of division reached i
            if len(path) == l:
                ans.append(path[:])
                return 

            for j in range(i,len(nums)):
               
                    path.append(nums[j])
                    dfs(j+1,path,l)
                    path.pop()  #pop only after the recursive call returns
            

        for l in range(len(nums)+1):
            dfs(0,[],l)
        return ans