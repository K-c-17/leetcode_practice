class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i=0
        while i*i<=x:
            target=i
            i+=1
        return target
        
        