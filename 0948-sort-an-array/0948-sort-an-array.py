class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)

        ans = []
        # print(nums)
        while nums:
            ans.append(heapq.heappop(nums))
        return ans