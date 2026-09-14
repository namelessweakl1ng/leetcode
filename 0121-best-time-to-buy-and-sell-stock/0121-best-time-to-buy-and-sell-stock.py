class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for p in prices[1:]:
            min_price = min(p,min_price)
            max_profit = max(p-min_price,max_profit)
        return max_profit