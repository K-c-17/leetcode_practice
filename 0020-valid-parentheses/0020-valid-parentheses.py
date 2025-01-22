class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_brac = '({['
        close_brac = ')}]'
        stack=[]
        mapping = {')':'(',']':'[','}':'{'}

        for i in s:
            if i in open_brac:
                stack.append(i)
            elif stack!=[] and i in close_brac:
                if mapping[i]==stack.pop():
                    pass
                else:
                    return False
            else:
                return False
        
        return False if stack!=[] else True
                    
