class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def count(s: str)->tuple:
            freq = [0 for i in range(26)]
            for c in s:
                freq[97 - ord(c)] += 1
            return tuple(freq)

        anagrams = defaultdict(list)
        for s in strs:
            key = count(s)
            anagrams[key].append(s)
        return list(anagrams.values())
