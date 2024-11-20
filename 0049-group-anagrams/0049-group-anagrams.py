class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            sorted_char = sorted(s)
            anagrams[tuple(sorted_char)].append(s)
        return list(anagrams.values())
           