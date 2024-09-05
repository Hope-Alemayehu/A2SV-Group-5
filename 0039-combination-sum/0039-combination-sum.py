class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #time complexity  O(N^(T/M) + N)
        #space complexity O(N)
        
        res = []
        n = len(candidates)
        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return 
            if remaining < 0 or start > n:
                return
            
            for i in range(start, n):
                c = candidates[i]
                path.append(c)
                backtrack(i, path, remaining - c)
                path.pop()


        backtrack(0, [], target)
        return res