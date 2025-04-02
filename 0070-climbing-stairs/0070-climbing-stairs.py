class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #divide and conquer without memoization
        '''
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            subP1=self.climbStairs(n-1)
            subP2=self.climbStairs(n-2)
            return subP1+subP2
        '''

        #Top down dp with memoization
        dp={}
        return self.climbStairs_helper(n,dp)
    
    def climbStairs_helper(self,n,dp):
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            if n not in dp:
                subP1=self.climbStairs_helper(n-1,dp)
                subP2=self.climbStairs_helper(n-2,dp)
                dp[n]=subP1+subP2
            return dp[n]

        