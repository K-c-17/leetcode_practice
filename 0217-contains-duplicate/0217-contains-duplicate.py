class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq=defaultdict(int)

        for i in nums:
            freq[i]+=1
        
        for j in freq.keys():
            if freq[j]>=2:
                return True

        return False
            