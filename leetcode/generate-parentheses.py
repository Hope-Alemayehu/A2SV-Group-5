class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(opens, close,path):
            if close > opens or opens > n:
                return
            if len(path) == 2*n:
                ans.append("".join(path.copy()))
                return
            
            dfs(opens + 1,close , path + ["("])
            dfs(opens, close + 1, path + [")"])

            return ans
        return dfs(0,0,[])