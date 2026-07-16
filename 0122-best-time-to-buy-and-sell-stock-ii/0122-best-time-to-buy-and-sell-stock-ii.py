class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)
        profit=0
        if(n<1):
            return 0
        for i in range(1,n):
            if(prices[i]>prices[i-1]):
                profit= profit+(prices[i]-prices[i-1])
        return profit
        