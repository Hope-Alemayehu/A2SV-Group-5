class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        #time complexity O(N)
        #space complexity O(1) not inlucding the returned list
        apointer = 0
        bpointer = 0
        res = []

        while apointer < len(A) and bpointer < len(B):
            AStart = A[apointer][0]
            AEnd = A[apointer][1]
            BStart = B[bpointer][0]
            BEnd = B[bpointer][1]
            
            #getting the intersection
            if AStart <= BEnd  and BStart <= AEnd:
                res.append([max(AStart,BStart),min(BEnd,AEnd)])
            
            #moving the pointers
            if AEnd < BEnd:
                apointer += 1
            else:
                bpointer += 1
        return res
        