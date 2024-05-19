class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        number_list=[i for i in str(x)]
        if tuple(number_list)==tuple(number_list[::-1]):
            return True
        else:
            return False
        