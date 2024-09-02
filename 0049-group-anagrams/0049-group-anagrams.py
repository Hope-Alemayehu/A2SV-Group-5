class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #time complexity
        #space complexity

        counter = {}

        for s in strs:
            sortedStr = sorted(s)
            sortedStr = "".join(sortedStr)
            #making sure the key exists
            if sortedStr not in counter:
                counter[sortedStr] = []
            counter[sortedStr].append(s)
        res = []
        for key, val in counter.items():
            res.append(list(val))
        return res

