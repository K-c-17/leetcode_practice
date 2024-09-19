class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stage=[]
        for i in asteroids:
            while len(stage)<>0 and i<0 and stage[-1]>0:
                top=stage.pop()
                if top>abs(i):
                    stage.append(top)
                    break
                elif top==abs(i):
                    break
                else:
                    continue
            else:
                stage.append(i)
        return stage


        