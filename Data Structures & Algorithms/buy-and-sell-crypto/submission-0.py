class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        buy_price_pointer, sell_price_pointer = 0, 1

        max_profit = 0

        while sell_price_pointer < len(prices):
            if prices[buy_price_pointer] < prices[sell_price_pointer]:
                profit = prices[sell_price_pointer] - prices[buy_price_pointer]
                max_profit = max(profit,max_profit)
            else:
                buy_price_pointer = sell_price_pointer
            sell_price_pointer += 1
        
        return max_profit