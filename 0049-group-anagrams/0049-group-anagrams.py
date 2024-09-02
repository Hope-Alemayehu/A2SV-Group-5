class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #time complexity O(N)
        #space complexity

        counter = {}

        for s in strs:
            sortedStr = sorted(s)
            sortedStr = "".join(sortedStr)
            #making sure the key exists
            if sortedStr not in counter:
                counter[sortedStr] = []
            counter[sortedStr].append(s)
        return list(counter.values())

