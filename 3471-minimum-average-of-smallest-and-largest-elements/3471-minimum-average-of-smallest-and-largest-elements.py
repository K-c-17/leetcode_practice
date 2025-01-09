class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        averages=[]
        lowest=0
        highest=0
        
        while len(nums)!=0:
            lowest=min(nums)
            highest=max(nums)
            averages.append((lowest+highest)/2.0)

            nums.remove(lowest)
            nums.remove(highest)

        return min(averages)
        