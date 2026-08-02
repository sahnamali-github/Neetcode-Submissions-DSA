class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # sell = 0
        # n = len(prices)
        # for i in range(n):
        #     sell = 0
        #     for j in range(i+1,n):
        #         sell = max(sell, prices[j])
        #     profit = max(profit , (sell - prices[i]))
        # return profit
        L = 0
        profit = 0
        for R in range(1, len(prices)):
            if prices[L] > prices[R]:
                L = R
            else:
                profit = max(profit, prices[R]-prices[L])
        return profit
         
        