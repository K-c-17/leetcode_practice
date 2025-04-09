class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # min heap based implementation
        stones=[-s for s in stones]
        heap=heapq.heapify(stones)

        while len(stones)>1:
            h=heapq.heappop(stones)
            sh=heapq.heappop(stones)
            result=abs(h)-abs(sh)

            heapq.heappush(stones,-1*result)
        
        return abs(stones[0])


        


        #O(N**2) Sorting implementation
        '''
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
        '''
            
        
            



        