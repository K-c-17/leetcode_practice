class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack,op,i=[],'+',0

        while i<len(s):
            if s[i].isdigit():
                num=''
                while i<len(s) and s[i].isdigit():
                    num+=s[i]
                    i+=1
                i-=1
                if op=='+':
                    stack.append(int(num))
                elif op=='-':
                    stack.append(-1*int(num)) 
                elif op=='*':
                    val=int(num)*stack.pop()
                    stack.append(val)
                elif op=='/':
                    val=int(float(stack.pop())/float(num))
                    stack.append(val)
            elif s[i] in ('+','-','*','/'):
                op=s[i]
            i+=1
        return sum(stack)


        