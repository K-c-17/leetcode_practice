class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        collector={}

        for i in arr:
            if i not in collector.keys():
                collector[i]=1
            else:
                collector[i]+=1
        
        unique_frequency=[]

        for j in collector.values():
            if j in unique_frequency:
                return False
            else:
                unique_frequency.append(j)
        return True