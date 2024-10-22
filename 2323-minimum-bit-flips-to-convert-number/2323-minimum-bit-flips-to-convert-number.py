class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        #better answer is here
        xor_result = start ^ goal
        ans = 0

        while xor_result > 0:
            ans += xor_result & 1
            #shifting it to the right or dividing it by 2
            xor_result >>= 1
        return ans
