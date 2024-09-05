class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        def backtrack(index, path):
            if len(path) == k:
                res.append(path[:])
                return
            if index >= n:
                return
            
            #not pick that number
            backtrack(index+1, path)

            #pick
            path.append(index+1)
            backtrack(index+1, path)
            path.pop()
        backtrack(0,[])
        return res
