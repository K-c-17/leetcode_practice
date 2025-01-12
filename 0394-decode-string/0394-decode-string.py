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
                    last_element=stack.pop()
                    if last_element!='[':
                        collector=last_element+collector
                    else:
                        freq=stack.pop()
                        while stack and stack[-1].isdigit():
                            prev_ele=stack.pop()
                            freq=prev_ele+freq
                        conc_string=int(freq)*collector
                        stack.append(conc_string)
                        break
        return ''.join(stack)
