class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        l,r=0,k
        maxS=sum(nums[l:r])
        final=maxS

        while r<len(nums):
            maxS-=nums[l]
            maxS+=nums[r]

            if maxS>final:
                final=maxS
            
            l+=1
            r+=1

        return (final*1.0)/k


        