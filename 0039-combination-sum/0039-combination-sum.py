class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        n = len(candidates)
        def backtrack(path, summ):
            if summ == 0:
                ans = path[:]
                ans.sort()
                res.add(tuple(ans))
                return 
            if summ < 0:
                return
            
            for c in candidates:
              
                path.append(c)
                summ -= c
                backtrack(path, summ)
                summ += path.pop()


        backtrack( [], target)
        return list(res)