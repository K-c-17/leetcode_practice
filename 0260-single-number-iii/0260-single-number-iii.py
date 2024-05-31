class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # multi_element= [i for i in nums if nums.count(i)==1]
        # return list(set(multi_element))
        collector={}
        for i in nums:
            collector[i]=collector.get(i,0)+1
        return [key for key,val in collector.items() if val==1]