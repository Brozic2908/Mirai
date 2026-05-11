class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        head=0
        tail=len(prices) - 1
        max_profit = 0

        while head < tail:
            profit = prices[tail] - prices[head]
            max_profit = max(profit, max_profit)

            if prices[head] > prices[tail]:
                head += 1
            else:
                tail -= 1
        
        return max(max_profit, 0)