class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #initializing the counters
        pos=0
        neg=0
        #traversal
        for i in nums:
            if i > 0:
                pos+=1
            elif i < 0:
                neg+=1
        
        return max(pos,neg)
