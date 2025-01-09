class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        collector={}
        final=0

        de_dup=[set(sorted(x)) for x in words]
        
        for i in de_dup:
            if tuple(i) not in collector:
                collector[tuple(i)]=1
            else:
                collector[tuple(i)]+=1
        
        freq=list(collector.values())

        for i in freq:
            final+=(i*(i-1))/2
        
        return final
        




        