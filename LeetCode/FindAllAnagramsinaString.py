class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s) :
            return []
        
        target = Counter(p)
        n = len(p)
        compare = defaultdict(int)
        for i in range (n):
            compare[s[i]] += 1

        res = []
        left = 0

        for i in range (n, len(s)):
            if compare == target:
                res.append(left)
            compare[s[left]] -= 1

            if compare[s[left]] == 0:
                del(compare[s[left]])

            compare[s[i]] += 1
            left += 1
        if compare == target:
            res.append(left)
        return res