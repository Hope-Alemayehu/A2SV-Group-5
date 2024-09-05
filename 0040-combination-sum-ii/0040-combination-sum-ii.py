class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #time complexity O(NlogN) + O(2^N)
        #space complexity O(N)
        res = []
        n = len(candidates)
        candidates.sort()
        def sumSubs(path,index, remaining):
            if remaining == 0: 
                res.append(path[:])
                return 
            if remaining <= 0:
                return

            #initalizing prev with -1 since noone has the value of -2
            prev = -1
            for i in range (index,n):
                c = candidates[i]
                if c == prev:
                    continue
                path.append(c)
                sumSubs(path,i+1, remaining - c)
                path.pop()

                prev = c
            return

        sumSubs([], 0,target)
        return res