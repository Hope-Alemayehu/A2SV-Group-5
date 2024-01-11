class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        vowels = ("a","e","i","o","u")
        left = 0
        res = float("-inf")
        for i in range(len(s)):
            if s[i] in vowels:
                count += 1
            window = i - left + 1
            if window == k:
                res = max(res , count)
                if s[left] in vowels:
                    count -= 1
                left += 1
        return res