class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        #time complexity O(2N)
        #space complexity O(N)
        hashi =  defaultdict(int)
        for x, y in matches:
            hashi[y] += 1

        list1 = set()
        list2 = set()
        for x, y in matches:
            if x not in hashi:
                list1.add(x)
            if hashi[y] == 1:
                list2.add(y)
        return [sorted(list(list1)), sorted(list(list2))]