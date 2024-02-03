class Solution:
    def maxScore(self, s: str) -> int:
        one = s.count("1")
        zero = 0
        left = []
        right = []
        for i in range(len(s) - 1):
            if s[i] == "0":
                zero += 1
                left.append(zero)  # Append zero, not left
                right.append(one)
            elif s[i] == "1":
                left.append(zero)
                one -= 1
                right.append(one)  # Append zero, not one
      
        res = 0
        for i in range (len(s)-1):
            res = max(res, left[i] + right[i])
        return res
