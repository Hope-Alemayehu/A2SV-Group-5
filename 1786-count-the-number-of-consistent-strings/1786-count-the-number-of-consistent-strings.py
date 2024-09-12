class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        check = set(allowed)
        for word in words:
            flag = True
            for c in word:
                if c not in check:
                    flag = False
            if flag:
                ans += 1
        return ans