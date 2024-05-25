class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        for i in range(0,len(nums)+1):
            if i not in nums:
                return i
        """
        return [i for i in range(0,len(nums)+1) if i not in nums][0] 
        