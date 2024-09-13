class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
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
        list1 = list(list1)
        list1.sort()
        list2 = list(list2)
        list2.sort()
        ans = [list1,list2]
        return ans