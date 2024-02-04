class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "" or t == "" or len(s) < len(t):
            return ""
        
        tHash = Counter(t)
        sHash = defaultdict(int)

        res = []
        reslen = float("inf")
        have , need = 0 , len(tHash)
        left = 0

        
        for i in range(len(s)):

            sHash[s[i]] += 1

            if s[i] in tHash and sHash[s[i]] == tHash[s[i]]:
                have += 1
            while have == need:
                if (i - left + 1) < reslen:
                    res = [left , i]
                    reslen = i - left + 1
                sHash[s[left]] -= 1
                if s[left] in tHash and sHash[s[left]] < tHash[s[left]]:
                    have -= 1
                left += 1
            
        if reslen != float("inf"):
            l , r = res
            return s[l:r + 1]
        else:
            return ""

