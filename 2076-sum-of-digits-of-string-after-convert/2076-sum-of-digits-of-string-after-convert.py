class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = []
        for c in s:
            num.append(str(ord(c) - ord("a")+1))
        while k:
            val = 0
            for s in num:
                for c in s:
                    val += int(c)
            num = [str(val)]
            k -= 1
        
        return int(num[-1])