class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        n = len(tickets)
        q = deque()
        for i in range(n):
            q.append([tickets[i],i])
        
        time = 0 #the number of people that left
        while q :
            tmpV,tmpI = q[0]
            q.popleft()
            if tmpV-1 >= 1:
                q.append([tmpV-1,tmpI])
            else:
                if tmpI == k:
                    return time + 1
            time += 1


      