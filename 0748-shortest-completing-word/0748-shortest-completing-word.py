class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        collector=[]
        sorLP=[val for val in licensePlate.lower() if val.isalpha()]
        for j in words:
            j=j.lower()
            if all([sorLP.count(i)<=j.count(i) for i in sorLP]):
                collector.append(j)
        sorted_collector=sorted(collector,key=lambda x: len(x))
        return sorted_collector[0]
        