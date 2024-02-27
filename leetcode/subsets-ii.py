class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        ans = []
        path = []
        def dfs(index):

            if index >= N:
                ans.append(path.copy())
                return
            path.append(nums[index])
            dfs(index+1)
            path.pop()

            while index+1 < N and nums[index] == nums[index+1]:
                index += 1
            dfs(index + 1)

            return ans
        dfs(0)
        return ans