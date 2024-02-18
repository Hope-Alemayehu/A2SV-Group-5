class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
       
        res = 0
        while target != 1:
            if target % 2 == 0 and maxDoubles:
                maxDoubles -= 1
                res += 1
                target = target // 2
            else:
                if maxDoubles == 0:
                    res += (target - 1)
                    return res
                else:
                    target -= 1
                    res += 1

        return res
