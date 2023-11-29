from typing import List

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        

        x = (num-3) / 3
        if x%1 != 0:
            return []
        else:
            x=int(x)
            return [x, x + 1, x + 2]
