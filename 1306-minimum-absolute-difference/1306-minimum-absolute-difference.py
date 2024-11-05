class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        N = len(arr) 
        minDiff = float("inf")
        arr.sort()
        ans = []

        for i in range(N-1):
            minDiff = min(minDiff, arr[i+1] - arr[i])

        for i in range(N - 1):
            if arr[i+1] - arr[i] == minDiff:
                ans.append([arr[i],arr[i+1]])
        return ans
