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
            else:
                if stack==[]:
                    return False
                else:
                    if mapping[i] != stack.pop():
                        return False
        return False if stack!=[] else True
                    
