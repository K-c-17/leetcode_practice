class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        #val=0
        stack,op,i=[],'+',0

        while i<len(s):
            #print("value of s[i] is:",s[i],i)
            if s[i].isdigit():
                num,j='',i
                while j<len(s) and s[j].isdigit():
                    num+=s[j]
                    j+=1
                i=j-1
                #print("the op is:",op)
                #print("the value of num: ",num)
                if op=='+':
                    #val=int(num)
                    stack.append(int(num))
                elif op=='-':
                    stack.append(-1*int(num)) 
                elif op=='*':
                    val=int(num)*stack.pop()
                    stack.append(val)
                elif op=='/':
                    #print("The value of stack and num is: ",stack[-1],num)
                    val=int(stack.pop()*1.0/int(num))
                    #print("The value of val:",val)
                    #print("The state of stack:",stack)
                    stack.append(val)
            elif s[i] in ('+','-','*','/'):
                op=s[i]
            #debugging
            #print(stack)
            i+=1
        return sum(stack)


        