class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = str(x)
        reverse = reverse[::-1]
        return str(x) == reverse