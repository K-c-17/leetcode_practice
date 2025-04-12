class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if (sum(nums)-target)%2 != 0 or sum(nums)<target:
            return 0
        
        s1=(sum(nums)-target)//2
        #print("s1: ",s1)

        return self.subsetSum(nums,s1)

    def subsetSum(self,arr,cap):
        n=len(arr)
        
        #intialization of matrix
        dp=[[0]*(cap+1) for _ in range(n+1)]
        #print(dp)
        for i in range(n+1):
            dp[i][0]=1
        
        for j in range(1,n+1):
            for k in range(cap+1):
                if arr[j-1]<=k:
                    dp[j][k]=dp[j-1][k-arr[j-1]] + dp[j-1][k]
                else:
                    dp[j][k]=dp[j-1][k]
        
        return dp[n][cap]


        