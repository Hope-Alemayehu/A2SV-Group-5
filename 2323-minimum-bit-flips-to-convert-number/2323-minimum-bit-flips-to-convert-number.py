class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        xor_binary = str(bin(xor))
        ans = 0 
        for c in xor_binary:
            if c == "1":
                ans += 1
        return ans