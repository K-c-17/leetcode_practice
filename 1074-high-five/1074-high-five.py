class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        collector={}
        for i in items:
            if i[0] not in collector.keys():
                collector[i[0]]=[i[1]]
            else:
                collector[i[0]].append(i[1])
        
        sorted_collector=[[key,sum(sorted(value,reverse=True)[0:5])/5] for key,value in collector.items()]

        return sorted_collector

        
        