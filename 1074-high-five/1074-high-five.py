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
        
        sorted_collector={key:sorted(value,reverse=True) for key,value in collector.items()}

        for id in sorted_collector.keys():
            sorted_collector[id]=sum(sorted_collector[id][0:5])/5
        

        top_five=[[a,b] for a,b in sorted_collector.items()]

        return top_five

        
        