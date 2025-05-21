class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def PalindromeRange(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                else:
                    l+=1
                    r-=1
            return True

        left,right=0,len(s)-1

        while left<right:
            if s[left]!=s[right]:
                return PalindromeRange(left,right-1) or PalindromeRange(left+1,right)
            else:
                left+=1
                right-=1
        
        return True


        