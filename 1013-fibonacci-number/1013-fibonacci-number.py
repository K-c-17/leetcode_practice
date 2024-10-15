class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        assert n>=0 and int(n)==n,"The input can only be non-negative integer"
        if n in [0,1]:
            return n
        #final function return
        return self.fib(n-2) + self.fib(n-1)
        