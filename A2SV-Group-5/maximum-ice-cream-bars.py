class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()
        count = 0

        for i in range(len(costs)):
            if costs[i]<=coins and coins:
                count += 1
                coins -= costs[i]
        return count
        