class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        mapping = {')':'(',']':'[','}':'{'}

        for i in s:
            if i in mapping.keys():
                top_element = stack.pop() if stack else 'dummy'

                if top_element!=mapping[i]:
                    return False
            
            else:
                stack.append(i)
        
        return True if not stack else False

