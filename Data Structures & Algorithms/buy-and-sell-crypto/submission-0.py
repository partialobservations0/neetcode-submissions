class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # at each point maintain curr profit
        # evaluate if i can sell and update profit
        # evaluate if i can reverse buy to this price
        currprofit = 0
        currbuy = 101
        for i,n in enumerate(prices):
            if n > currbuy: 
                currprofit = max(currprofit, (n - currbuy))
            else:
                currbuy = n
        return currprofit