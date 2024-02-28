class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        mapp = {"2":["a","b","c"],"3":["d","e","f"],
                "4":["g","h","i"],"5":["j","k","l"],
                "6":["m","n","o"],"7":["p","q","r","s"],
                "8":["t","u","v"],"9":["w","x","y","z"]}
        N = len(digits)
        if N == 1:
            return mapp[digits[0]]
        if N == 0:
            return ""

        def dfs(index,path):
            if len(path) == N:
                ans.append("".join(path.copy()))
                return
            
            for ch in mapp[digits[index]]: 
                path.append(ch)
                dfs(index+1, path)
                path.pop()
        dfs(0,[])
        return ans