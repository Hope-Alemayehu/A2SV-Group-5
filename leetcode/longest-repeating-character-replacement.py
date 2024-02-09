class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = float("-inf")
        visited = set()
        n = len(s)

        for c in s:
            if c in visited:
                continue
            else:
                left = 0
                count = 0
                for i in range (n):
                    if s[i] != c:
                        count += 1
                    while count > k:
                        if s[left] != c:
                            count -= 1
                        left += 1
                    res = max(res,i - left + 1)
                    
                visited.add(c)
        return res

