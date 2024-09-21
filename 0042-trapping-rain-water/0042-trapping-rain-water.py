class Solution:
    def trap(self, height: List[int]) -> int:
        #time complexity O(N)
        #space complexity O(N)
        n = len(height)
        minLeft = [0]
        minRight = [0 for i in range(n)]

        for i in range(n - 1):
            minLeft.append(max(minLeft[-1], height[i]))

        for i in range(n-2, -1, -1):
            minRight[i] = max(height[i+1], minRight[i+1])
        # print(minLeft)
        # print(minRight)
        ans = 0
        for i in range(n):
            cur = min(minLeft[i],minRight[i]) - height[i]
            if cur > 0:
                ans += cur

        return ans
