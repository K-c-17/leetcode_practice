class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t_s=[lower(x) for x in s if x.isalnum()]

        return t_s[::]==t_s[::-1]























        # left=0
        # right=len(s)-1

        # while left<right:
        #     if s[left].isalnum() and s[right].isalnum():
        #         if s[left].lower() != s[right].lower():
        #             print(s[left],s[right])
        #             return False
        #         else:
        #             left+=1
        #             right-=1
        #     else:
        #         if not s[left].isalnum():
        #             left+=1
        #         if not s[right].isalnum():
        #             right-=1
            
        # return True



        # left=0
        # right=len(s)-1

        # while right>=left:
        #     if s[left].isalnum() and s[right].isalnum():
        #         if s[left].lower() != s[right].lower():
        #             return False
        #         left+=1
        #         right-=1
        #     else:
        #         if not s[left].isalnum():
        #             left+=1
        #         if not s[right].isalnum():
        #             right-=1


        # return True