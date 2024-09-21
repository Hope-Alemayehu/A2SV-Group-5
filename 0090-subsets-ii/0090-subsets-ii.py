class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        n = len(nums)

        def dfs(index, path):
            if index == n:
                res.add(tuple(path[:]))
                return 
            
            dfs(index +1, path)

            path.append(nums[index])
            dfs(index+1, path)
            path.pop()
        
        dfs(0,[])
        return list(res)