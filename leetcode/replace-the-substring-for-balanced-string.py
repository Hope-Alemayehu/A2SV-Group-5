class Solution:
    def balancedString(self, s: str) -> int:
        count =defaultdict(int)
        
        for i in range (len(s)):
            count[s[i]] += 1
      
      
        balance = len(s)/4
        minlen = len(s)
        left = 0
        for i in range(len(s)):
            count[s[i]] -= 1

            while (left < len(s) and
                    count["Q"] <= balance and
                    count["W"] <= balance and
                    count["E"] <= balance and
                    count["R"] <= balance):
                minlen = min(minlen , i - left + 1)
                count[s[left]] += 1
                left += 1
        return minlen