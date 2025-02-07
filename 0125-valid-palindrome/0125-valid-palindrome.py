class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left=0
        right=len(s)-1

        while right>=left:
            print("left:",s[left])
            print("right:",s[right])
            
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
                left+=1
                right-=1
            else:
                if not s[left].isalnum():
                    left+=1
                if not s[right].isalnum():
                    right-=1


        return True