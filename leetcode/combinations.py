class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #time complexity = O(2)
        ans = []

        def backtrack(i,path):
            #base case
            if len(path) == k:
                ans.append(path[:])
                return  # return after appending to ans , there is no need to pop here
            
            #optimization
            need = k - len(path)
            remain = n - i + 1
            available = remain - need

            for j in range(i,i + available + 1):
                path.append(j)
                backtrack(j+1,path)
                path.pop()  #pop only after the recursive call returns
        
        #we shouldn't pass n here because we want it to start from one
        backtrack(1,[])
        return ans

