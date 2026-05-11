class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        head=0
        tail=len(prices) - 1
        max_profit = 0
        min_price = price[0]

        for price in prices:
            if min_price >= price:
                min_price = price
            
            profit = price - min_price
            max_profit = max(profit, max_profit)

        return max(max_profit, 0)