class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = list(senate)

        while (len(set(q)) != 1):
            if q[0] == "R":
                q.remove("D")
                q.remove("R")
                q.append("R")
            else:
                q.remove("R")
                q.remove("D")
                q.append("D")
        if q[0] == "D":
            return "Dire"
        else:
            return "Radiant"