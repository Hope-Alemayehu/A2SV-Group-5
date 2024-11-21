class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = defaultdict(int)
        for i in range(len(s)):
            seen[s[i]] += 1
            
        for i in range(len(s)):
            if seen[s[i]] == 1:
                return i
        return -1