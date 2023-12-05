class Solution:
    def numberOfMatches(self, n: int) -> int:
        #time complexity O(Log n)
        #space complexity O(1)
        if n==1:
            return 0
        if n==2:
            return 1
        team=n
        matches=0
        while team>1:
            if team%2==0:
                matches+=team/2
                team=team/2
               
            elif team%2!=0:
                matches+=(team-1)/2
                team=(team-1)/2+1
            if team==2:
                matches+=1
                return int(matches)
        