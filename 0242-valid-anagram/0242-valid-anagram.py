class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #get the count of each character for s
        #iterate through the string of t while minimizing the frequency of t
        #check if the dictionary is empty in the end
        if len(s) != len(t):
            return False
        freq = {}
        for c in t:
            freq[c] = freq.get(c,0) + 1
        
        for c in s:
            if c in freq:
                freq[c] -= 1
                if freq[c] == 0:
                    del(freq[c])
        # print(freq)
        return len(freq) == 0
