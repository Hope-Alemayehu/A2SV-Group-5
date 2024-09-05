class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []

        ans = []
        k = 0
        while k < len(original):
            ans.append(original[k:k+n])
            k += n
        return ans