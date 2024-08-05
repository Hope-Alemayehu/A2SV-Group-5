class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)

        for num in arr:
            if freq[num] == 1:
                k -= 1
            
            if k == 0:
                return num

        return ""