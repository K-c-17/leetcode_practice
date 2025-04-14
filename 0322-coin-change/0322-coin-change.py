class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n=len(coins)
        t=amount
        
        dp=[[0]*(t+1) for _ in range(n+1)]

        for k in range(t+1):
            dp[0][k]=float("inf")
        
        for l in range(1,t+1):
            if l%coins[0]==0:
                dp[1][l]=l//coins[0]
            else:
                dp[1][l]=float("inf")

        for i in range(2,n+1):
            for j in range(1,t+1):
                if coins[i-1]<=j:
                    dp[i][j]=min(dp[i][j-coins[i-1]]+1,dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        #print(dp)
        
        if dp[n][t]!=float("inf"):
            return dp[n][t]
        else:
            return -1