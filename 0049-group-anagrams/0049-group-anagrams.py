class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = defaultdict(list)
        for st in strs:
            c = sorted(st)
            check[str(c)].append(st)

        return list(check.values())