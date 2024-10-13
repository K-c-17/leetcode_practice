import math
class Solution(object):
    
    def eatsAll(self,piles,k,h):
        hours=0
        for i in piles:
            banana_hours=i//k
            if i%k != 0:
                banana_hours += 1
            hours+=banana_hours
            
            if hours>h:
                return False
        return True

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left,right = 1,max(piles)
        
        while left<=right:
            middle=(left+right)//2

            if self.eatsAll(piles,middle,h):
                right= middle - 1
                response=middle
            else:
                left= middle + 1
        return response