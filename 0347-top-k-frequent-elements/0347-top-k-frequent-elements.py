class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq=collections.Counter(nums)
        
        # return sorted(freq,key=freq.get,reverse=True)[:k]
        
        return heapq.nlargest(k,freq,key=freq.get)




        