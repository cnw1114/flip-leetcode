class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        for start in range(len(prices)):
            sell_price = max(prices[start:])
            if sell_price > prices[start]:
                output = max(sell_price-prices[start], output)
        return output
