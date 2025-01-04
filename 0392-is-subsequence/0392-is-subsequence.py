class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # is_match=0
        # match_index=float('-inf')
        # for i in range(len(s)):
        #     for j in range(len(t)):
        #         if s[i]==t[j] and j>match_index:
        #             match_index=j
        #             is_match+=1
        #             break
        # if is_match==len(s):
        #     return True
        # else:
        #     return False
        
        is_match=0
        i=0
        j=0
        while j<=len(t)-1 and i<=len(s)-1:
            if s[i]==t[j]:
                is_match+=1
                i+=1
            j+=1
        if i==len(s):
            return True
        else:
            return False
                    


        