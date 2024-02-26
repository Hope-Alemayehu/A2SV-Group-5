class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []
        check = set()   #to not repeat characters 
        def dfs(num , check):
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for num in nums:
                if num not in check:
                    path.append(num)
                    check.add(num)
                    dfs(path,check.copy())      #we have to pass check as reference so that 
                                            #the changes made in one recursive call don't affect the other
                    path.pop()
                    check.remove(num)
                
        dfs(path,check)
        return ans
