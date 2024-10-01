class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        m = []
        N = len(arr)

        for i in range(N):
            m.append(arr[i]%k)
     
     
        m.sort()
        left = 0

        while  left < N and m[left] == 0 :
            left += 1
        if (left % 2) != 0:
            return False

        right = N - 1

        while left < right:
            if m[left] + m[right] != k:
                return False
            left += 1
            right -= 1
        return True