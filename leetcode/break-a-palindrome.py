class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""

        s = list(palindrome)
        for i in range(len(s) // 2):
            if s[i] != 'a':
                s[i] = 'a'
                return "".join(s)
        
        # If we're here, it means all characters are 'a' except the last one
        s[-1] = 'b'
        return "".join(s)
