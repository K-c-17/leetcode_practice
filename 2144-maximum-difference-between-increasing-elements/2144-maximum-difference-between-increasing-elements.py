class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=1
        maxD=-float('inf')

        while j<len(nums):
            if nums[j]>nums[i]:
                diff=nums[j]-nums[i]
                maxD=max(diff,maxD)
            elif nums[j]<nums[i]:
                i=j
            j+=1
        if maxD>=0:
            return maxD
        else:
            return -1

        