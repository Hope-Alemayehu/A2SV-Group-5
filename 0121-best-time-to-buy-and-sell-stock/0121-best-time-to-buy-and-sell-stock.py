class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Dp approch
        #time complexity O(N)
        #space complexity O(N)
        min_prices = [prices[0]]
        for i in range(1,len(prices)):
            min_prices.append(min(prices[i], min_prices[i-1]))
        # print(min_prices)
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - min_prices[i])

        return max_profit