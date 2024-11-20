class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        #brute force approch
        N = len(prices)
        # for i in range(N - 1):
        #     for j in range(i+1,N):
        #         profit = max(profit, (prices[j] - prices[i]))
        # return profit

        #optimized approch
        buy, sell = 0, 1
        while buy < sell and sell < N:
            cur_profit = prices[sell] - prices[buy]
            if cur_profit < 0:
                buy = sell
                sell += 1
                continue
            profit = max(cur_profit, profit)
            sell += 1
        return profit
            