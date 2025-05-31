class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums=[str(x) for x in nums]

        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                if nums[j]+nums[j+1]<nums[j+1]+nums[j]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        
        res=''.join(nums)
        
        return '0' if res[0]=='0' else res








        
        