class Solution:
    def isPalindrome(self, s: str) -> bool:
        #time complexity O(N)
        #space complexity O(M) M being the length of the string
    
        left , right = 0 ,len(s)-1

        while left<right:
            #checking if its alpnum
            
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if  left < right  and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True