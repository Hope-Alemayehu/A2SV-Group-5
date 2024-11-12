class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #create a hashmap for counting
        freq = defaultdict(int)
        #intalize the left and right pointers
        left, right = 0, 0
        #intalize the result to have smallest possible value
        result = 0
        #iterate through the string
        for right in range(len(s)):
            freq[s[right]] += 1
            #remove duplicates
            while freq[s[right]] == 2:
                freq[s[left]] -= 1
                left += 1
            #update the result
            result = max(result, right - left + 1)
        return result 
