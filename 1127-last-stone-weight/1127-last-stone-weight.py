class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        def smash(y,x):
            if x==y:
                return 0
            else:
                return abs(y-x)
        
        while len(stones)>1:
            stones.sort()
            h=stones.pop()
            sh=stones.pop()
            #print("Value of highest:",h)
            #print("Value of second highest:",sh)
            result=smash(h,sh)
            stones.append(result)
            #print("Stones",stones)
        
        return stones[0]
            
        
            



        