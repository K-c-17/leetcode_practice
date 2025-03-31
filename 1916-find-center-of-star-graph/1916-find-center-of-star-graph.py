class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        connect=defaultdict(int)
        #connect=[0]*(len(edges)+2)

        for i in edges:
            connect[i[0]]+=1
            connect[i[1]]+=1
        
        #for j in range(1,len(connect)+2):
        for j in connect:
            if connect[j]>1:
                return j
        return -1
        