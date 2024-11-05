class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #initalize a dictionary for counting
        freq = defaultdict(int)
        #start moving through the string while counting
        left = 0
        N = len(s)
        result = 0

        for i in range(N):
        
            freq[s[i]] += 1
            #if the count of one character > 1 minimize the window from the left
            while freq[s[i]] == 2:
                
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del(freq[s[left]])
                left += 1
            result = max(result, i - left + 1)
        return result
  
