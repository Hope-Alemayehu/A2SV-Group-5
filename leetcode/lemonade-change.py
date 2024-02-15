class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        numberof5 = 0
        count10 = 0
        for b in bills:
            if b == 5:
                numberof5 += 1
            elif b == 10:
                numberof5 -= 1
                count10 += 1
                if numberof5 < 0:
                    return False
            else:
                if numberof5 >= 1 and count10 >= 1:
                    numberof5 -= 1
                    count10 -= 1
                elif numberof5 >= 3:
                    numberof5 -= 3
                else:
                    return False
        return True 

            

        return True
            

