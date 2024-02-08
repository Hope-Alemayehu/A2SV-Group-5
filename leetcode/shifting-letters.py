class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        #time complexity O(3N) - N being the length of string
        #space complexity O(2N)

        n = len(s) 
        res = []
        prefix = [0] * n

        #to help us intialize the prefix with out doing calculation
        for i in range (n):
            prefix[0] += shifts[i]
            if i+1 < n:
                prefix[i+1] -= shifts[i]

        #building the prefix sum
        for i in range (1,n):
            prefix[i] += prefix[i-1]
       
        for i,c in enumerate (s):
            # shifts = prefix[i] % 26
            # res.append(chr(ord(c) + shifts))

            val = prefix[i] + ord(c)
            res.append(chr((val - 97) % 26 + 97))
        return "".join(res)