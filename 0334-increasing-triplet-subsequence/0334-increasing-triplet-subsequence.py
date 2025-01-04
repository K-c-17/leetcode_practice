class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        var1=float("inf")
        var2=float("inf")
        
        for i in nums:
            if i<=var1:
                var1=i
            elif i<=var2:
                var2=i
            else:
                return True
        return False
        