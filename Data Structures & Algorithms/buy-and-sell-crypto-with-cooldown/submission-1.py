class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for buying in [1, 0]: # state: buying is 1, selling is 0
                if buying:
                    buy = dp[i + 1][0] - prices[i] if i + 1 < n else -prices[i]
                    cooldown = dp[i + 1][1] if i + 1 < n else 0
                    dp[i][1] = max(buy, cooldown)

                else:
                    sell = dp[i + 2][1] + prices[i] if i + 2 < n else prices[i]
                    cooldown = dp[i + 1][0] if i + 1 < n else 0
                    dp[i][0] = max(sell, cooldown)

        return dp[0][1]
