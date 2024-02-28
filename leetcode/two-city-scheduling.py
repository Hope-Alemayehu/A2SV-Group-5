class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        #time complexity O(NlogN) since we sorted it
        #space complexity = O(1)

        res = 0
        #we are sorting it based on the profit and 
        costs = sorted(costs,key = lambda x: x[0] - x[1])

        n = len(costs)
        for i in range(n):
            #to get the minimum cost we gotta take the first one for the 
            #first half and take the second element for the second half
            if i < n/2 :
                res += costs[i][0]
            else:
                res += costs[i][1]
        return res