class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n=len(coins)
        t=amount

        dp=[[0]*(t+1) for _ in range(n+1)]

        for k in range(n+1):
            dp[k][0]=1
        
        for i in range(1,n+1):
            for j in range(1,t+1):
                if coins[i-1]<=j:
                    dp[i][j]=dp[i][j-coins[i-1]] + dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        
        #print(dp)
        return dp[n][t]

        