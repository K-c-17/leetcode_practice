class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #O(n) time complexity
        if len(nums)==1:
            return nums
     
        #reverse the entire array
        start=0
        last=len(nums)-1

        while start<last:
            nums[start],nums[last]=nums[last],nums[start]
            start+=1
            last-=1
        
        #reverse the first k elements
        start=0
        last=k%len(nums) - 1

        while start<last:
            nums[start],nums[last]=nums[last],nums[start]
            start+=1
            last-=1
        
        #reverse the last len(nums)-k elements
        start=k%len(nums)
        last=len(nums)-1

        while start<last:
            nums[start],nums[last]=nums[last],nums[start]
            start+=1
            last-=1
        
        return nums
