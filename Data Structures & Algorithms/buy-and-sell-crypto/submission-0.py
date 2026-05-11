class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=0
        max=len(prices) - 1
        max_profit = 0

        while min < max:
            profit = prices[max] - prices[min]
            profit = max(profit, max_profit)

            if prices[min] < prices[max]:
                min += 1
            else:
                max -= 1
        
        return max(max_profit, 0)