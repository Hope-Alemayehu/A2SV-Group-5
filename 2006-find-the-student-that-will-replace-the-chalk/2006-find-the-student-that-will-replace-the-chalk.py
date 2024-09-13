class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        total  = sum(chalk)
        k = k % total 
        i = 0
        while  k :
            i = 0 + i%n
            k -= chalk[i]
            if k < 0:
                return i
            i += 1
        return i%n
        
