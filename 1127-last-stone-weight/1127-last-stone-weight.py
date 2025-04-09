class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        def smash(x,y):
            if x==y:
                return 0
            else:
                return abs(y-x)
        
        while len(stones)>1:
            stones.sort()
            h=stones.pop()
            sh=stones.pop()
            result=smash(h,sh)
            stones.append(result)
        
        return stones[0]
            
        
            



        