class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner=set()
        loser=set()
        losercount=defaultdict(int)
        n=len(matches)
        for win,loss in matches:
            winner.add(win)
            loser.add(loss)
            losercount[loss]+=1

        res=[[],[]]
        for win in winner:
            if win in loser:
                continue
            res[0].append(win)
        for loss in losercount:
            if losercount[loss]==1:
                res[1].append(loss)
        res[0].sort()
        res[1].sort()
        return res
        