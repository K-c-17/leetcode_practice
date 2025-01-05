class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if i==len(nums)-1:
                suffix=0
            else:
                suffix=sum(nums[i+1:])
            
            if i==0:
                prefix=0
            else:
                prefix=sum(nums[:i])
            
            if prefix==sum(nums[i+1:]):
                return i
        return -1
        