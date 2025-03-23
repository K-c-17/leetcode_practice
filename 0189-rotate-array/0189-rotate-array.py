class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        final=[None for _ in nums]
        size=len(nums)
        for r in range(size):
            if r+k<size:
                final[r+k]=nums[r]
            else:
                loop=(r+k)//size
                final[r+k-(loop*size)]=nums[r]
        nums[:]=final
        
        return nums