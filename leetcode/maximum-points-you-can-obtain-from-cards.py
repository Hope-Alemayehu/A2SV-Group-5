class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        total = sum(cardPoints)
        cur = 0
        res = 0
        #creating the first window
        
        for i in range(len(cardPoints)-k):
            cur += cardPoints[i]

        res = total - cur
        left = 0
        r = len(cardPoints) - k
        while r < len(cardPoints):
            cur -= cardPoints[left]
            cur += cardPoints[r]
            res = max(res, total - cur)

            left += 1
            r += 1
        return res
            


