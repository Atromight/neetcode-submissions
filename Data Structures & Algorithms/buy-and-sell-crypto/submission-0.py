class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        i = 0
        j = 1 
        while i <= j and j < n:
            if prices[i] > prices[j]:
                i = j
            elif prices[i] <= prices[j]:
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit

            j += 1

        return max_profit
