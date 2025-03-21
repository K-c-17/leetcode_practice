class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=1

        while r<len(nums):
            if nums[l]==nums[r]:
                r+=1
            else:
                nums[l+1],nums[r]=nums[r],nums[l+1]
                l+=1
                r+=1
        
        return len(nums[0:l+1])

        
        
        
        
        
        
        '''
        i=1
        while i!=len(nums):
            if nums[i]==nums[i-1]:
                nums.remove(nums[i-1])
            else:
                i+=1
        
        return len(nums)
        '''

        