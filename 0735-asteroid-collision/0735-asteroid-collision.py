class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]
        for i in asteroids:
            while stack and stack[-1]>0 and i<0:
                diff=stack[-1]-abs(i)
                if diff>0:
                    i=0
                elif diff<0:
                    stack.pop()
                else:
                    stack.pop()
                    i=0
            if i:
                stack.append(i)
        return stack
        


        