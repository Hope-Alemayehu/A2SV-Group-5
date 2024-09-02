class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #time complexity O(N*M)
        #space complexity O(N*M)

        freq = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord("a")] += 1
            freq[tuple(count)].append(s)
        return list(freq.values())

