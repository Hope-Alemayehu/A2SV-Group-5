class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(index,path):
            if index == n:
                res.append(path[:])
                return
            #no pick 
            dfs(index +1,path)

            #pick
            path.append(nums[index])
            dfs(index+1,path)
            path.pop()
        
        dfs(0,[])
        return res
            
