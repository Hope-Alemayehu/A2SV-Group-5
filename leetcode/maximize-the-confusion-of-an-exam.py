class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        if len(answerKey) == 1:
            return 1
        
        m = 0
        left = 0
        res = 0

        # Change all to True
        for r in range(len(answerKey)):
            if answerKey[r] == "F":
                m += 1
            while m > k and left < len(answerKey):
                if answerKey[left] == "F":
                    m -= 1
                left += 1
            res = max(res, r - left + 1)
        
        m = 0
        left = 0
        # Change all to False
        for r in range(len(answerKey)):
            if answerKey[r] == "T":
                m += 1
            while m > k and left < len(answerKey):
                if answerKey[left] == "T":
                    m -= 1
                left += 1
            res = max(res, r - left + 1)

        return res
