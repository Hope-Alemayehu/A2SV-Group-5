class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        y_penality = [0]*(n+1)
        n_penality = [0]*(n+1)

        #to construct the pernalities
        for i in range (n):
            if customers[i] == "Y":
                y_penality[i] = 1
            else:
                n_penality[i+1] = 1
            
        #make the prefix
        for i in range (n-1,-1,-1):
            y_penality[i] += y_penality[i+1]
             
        for i in range (1,n+1):
            n_penality[i] += n_penality[i-1]
        
        res = float("inf")
        idx = n+1

        for i in range (n+1):
            y_penality[i] += n_penality[i]
          
            if y_penality[i] < res:
                res = y_penality[i]
                idx = i
        return idx

      
