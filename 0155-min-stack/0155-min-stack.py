class MinStack(object):

    def __init__(self):
        self.arr=[]
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.arr)==0:
            self.arr.append((val,val))
        else:
            min_val=min(self.arr[-1][1],val)
            self.arr.append((val,min_val))
        
        

    def pop(self):
        """
        :rtype: None
        """
        self.arr.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.arr[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()