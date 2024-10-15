class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in [0,1]:
            return n
        #final function return
        return self.fib(n-2) + self.fib(n-1)
        