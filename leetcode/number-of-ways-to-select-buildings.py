class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros = s.count("0")
        ones = len(s) - zeros
        zeroprefix = 0
        oneprefix = 0
        res = 0

        for c in s:
            if c == '0':
                res += oneprefix *(ones- oneprefix)
                zeroprefix += 1
            else:
                res += zeroprefix *(zeros - zeroprefix)
                oneprefix += 1
        return res