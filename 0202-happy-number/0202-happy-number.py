class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        number=n
        seen=set()

        while True:

            computed=0
            
            for i in str(number):
                computed+=int(i)**2
            
            number=computed

            if number==1:
                return True
            elif number in seen:
                return False
            else:
                seen.add(number)