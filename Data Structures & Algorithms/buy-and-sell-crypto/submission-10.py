class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        max_p = 0

        while R < len(prices):
            if prices[R] > prices[L]:
                profit = prices[R] - prices[L]
                max_p = max(max_p, profit)
            else:
                L = R
            R += 1

        return max(0, max_p)