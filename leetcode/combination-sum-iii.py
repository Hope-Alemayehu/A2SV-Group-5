class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = set()

        def dfs(index,path):
            if len(path) == k and sum(path) == n:
                ans.add(tuple(path.copy()))
                return
            for j in range(index,10):
                if sum(path) + j > n:
                    return
                
                path.append(j)
                dfs(j+1,path)
                path.pop()

        for i in range(1,10):
            dfs(i,[])
        return ans
