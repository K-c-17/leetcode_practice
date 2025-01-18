class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        collector={}
        for i in range(len(numbers)):
            comp=target-numbers[i]
            if numbers[i] not in collector.keys():
                collector[comp]=i
            else:
                return [collector[numbers[i]]+1,i+1]
        