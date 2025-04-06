class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total=sum(nums)

        if total%2!=0:
            return False
        else:
            return self.subSum(nums,total/2)
    

    def subSum(self,arr,target):
        '''
        Checks if any subset of the array 
        sums upto target
        '''
        n=len(arr)

        dp=[[False]*(target+1) for _ in range(n+1)]

        for k in range(n+1):
            dp[k][0]=True
        
        for i in range(1,n+1):
            for j in range(1,target+1):
                if arr[i-1]<=target:
                    dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        
        return dp[n][target]
        
        