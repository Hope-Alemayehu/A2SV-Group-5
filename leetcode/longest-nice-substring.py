class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)

        if n < 2:
            return ""
        s_set = set(s)
        for i in range(n):
            if s[i].swapcase() not in s_set:
                s1 = self.longestNiceSubstring(s[0:i])
                s2 = self.longestNiceSubstring(s[i+1:])

                if len(s1) >= len(s2):
                    return s1
                else:
                    return s2
        return s
