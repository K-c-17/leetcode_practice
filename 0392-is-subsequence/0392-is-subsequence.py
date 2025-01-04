class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        is_match=0
        i=0
        j=0
        while j<=len(t)-1 and i<=len(s)-1:
            if s[i]==t[j]:
                is_match+=1
                i+=1
            j+=1
        if is_match==len(s):
            return True
        else:
            return False
                    


        