class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force solution
        N = len(nums)
        # for i in range(N):
        #     for j in range(i + 1, N):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
       

        #optimized solution
        indexMap = defaultdict(int)
        for i in range(N):
            reminder = target - nums[i]
            if reminder in indexMap:
                return [indexMap[reminder], i]
            indexMap[nums[i]] = i
        