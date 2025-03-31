class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        connect=defaultdict(int)

        for i in edges:
            connect[i[0]]+=1
            connect[i[1]]+=1
        
        for j in connect:
            if connect[j]>1:
                return j
        