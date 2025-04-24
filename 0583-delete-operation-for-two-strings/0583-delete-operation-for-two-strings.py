class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        lcs_len=self.lcs(word1,word2)
        return (len(word1)+len(word2)-2*lcs_len)
    
    def lcs(self,x,y):
        m,n=len(x),len(y)
        dp=[[-1]*(n+1) for _ in range(m+1)]

        #initialize
        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j==0:
                    dp[i][j]=0
        
        #choice diagram
        for i in range(1,m+1):
            for j in range(1,n+1):
                if x[i-1]==y[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        
        return dp[m][n]
        

        