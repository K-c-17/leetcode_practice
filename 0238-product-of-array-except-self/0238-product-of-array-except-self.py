class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        prefix=[1]*n
        suffix=[1]*n
        final=[1]*n

        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]
        
        for j in range(n-2,-1,-1):
            suffix[j]=suffix[j+1]*nums[j+1]
        
        counter=0
        for a,b in zip(prefix,suffix):
            final[counter]=a*b
            counter+=1
        
        return final