class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums)==1:
        #     nums.remove(nums[0])
        #     print(nums)
        #     return len(nums)
        i=1
        while i!=len(nums):
            if nums[i]==nums[i-1]:
                nums.remove(nums[i-1])
            else:
                i+=1
        
        return len(nums)

        