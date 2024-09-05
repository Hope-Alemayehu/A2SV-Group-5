class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        
        N = len(pattern)
        for w in words:
            flag = True
            hashi = {}
            check = set()
            for i in range(N):
                if pattern[i] not in hashi and w[i] not in check:
                    hashi[pattern[i]] = w[i]
                    check.add(w[i])
                elif pattern[i] not in hashi or w[i] not in check:
                    flag = False
                    break
                else:
                    if hashi[pattern[i]] != w[i]:
                        flag = False
                        break
            if flag:
                ans.append(w)
        return ans

