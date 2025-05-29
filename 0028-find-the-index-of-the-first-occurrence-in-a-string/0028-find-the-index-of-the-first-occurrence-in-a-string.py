class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        diff=len(haystack)-len(needle)
        x=len(needle)
        i=0

        if diff==0:
            if haystack==needle:
                return 0
            else:
                return -1


        while i<=diff:
            if haystack[i:i+x]==needle:
                return i
            else:
                i+=1
        return -1


        