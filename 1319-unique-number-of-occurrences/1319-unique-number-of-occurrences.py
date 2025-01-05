class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        collector={i:arr.count(i) for i in arr}
        unique_frequency=[]

        for j in collector.values():
            if j in unique_frequency:
                return False
            else:
                unique_frequency.append(j)
        return True