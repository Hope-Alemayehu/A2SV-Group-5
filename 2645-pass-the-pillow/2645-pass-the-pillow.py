class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time < n:
            return 1 + time
        else:
            round = time //(n-1)
            step = time % (n-1)

            #even round means its coming from 1 to n
            if round % 2 == 0:
                return 1 + step
            #odd round is when we are going from n to 1
            else:
                return n - step