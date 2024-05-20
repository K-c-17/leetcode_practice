class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        collector={}
        for i in strs:
            sorted_str=''.join(sorted(i))
            if sorted_str not in collector:
                collector[sorted_str]=[i]
            else:
                collector[sorted_str].append(i)
        return [val for val in collector.values()]
            
            
            
        