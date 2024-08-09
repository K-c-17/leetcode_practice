class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=0
        r=1
        maxProfit=0

        while r < len(prices):
            if prices[r]>prices[l]:
                profit=prices[r]-prices[l]
                maxProfit=max(maxProfit,profit)
            else:
                l=r
            r+=1
        
        return maxProfit

        