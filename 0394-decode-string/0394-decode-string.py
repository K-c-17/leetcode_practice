class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in s:
            if i !=']':
                stack.append(i)
            else:
                collector=''
                while True:
                    print("Before digit extraction, stack:",stack)
                    last_element=stack.pop()
                    if last_element!='[':
                        collector=last_element+collector
                    else:
                        freq=stack.pop()
                        while stack and stack[-1].isdigit():
                            prev_ele=stack.pop()
                            freq=prev_ele+freq
                        print('frequency',freq)
                        print('stack',stack)
                        print('Reverse version of string:',collector[::-1])
                        conc_string=int(freq)*collector
                        print(conc_string)
                        stack.append(conc_string)
                        print('Final state of stack:',stack)
                        break
        return ''.join(stack)
