class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]

        for i in range(len(s)):
            if s[i] in ('(',')'):
                if stack and s[i]==')' and s[stack[-1]]=='(':
                    stack.pop()
                else:
                    stack.append(i)
        
        final,j=[],0
        stack=set(stack)
        #print(stack)
        while j<len(s):
            if j not in stack:
                final.append(s[j])  
            j+=1
        return ''.join(final)


                





            
        