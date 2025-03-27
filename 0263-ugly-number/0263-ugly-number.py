from math import sqrt
class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        curr=n

        if curr<=0:
            return False
        
        while curr!=1:
            if curr%2==0:
                curr=curr//2
            elif curr%3==0:
                curr=curr//3
            elif curr%5==0:
                curr=curr//5
            else:
                return False
        
        return True



        