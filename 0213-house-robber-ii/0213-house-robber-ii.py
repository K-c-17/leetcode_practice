class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
            
        nums1=nums[:len(nums)-1]
        nums2=nums[1:len(nums)]
        # print(nums1)
        # print(nums2)
        def rob_helper(x):
            rob1,rob2=0,0

            for i in x:
                temp=max(i+rob1,rob2)
                rob1=rob2
                rob2=temp
            return rob2
        
        return max(rob_helper(nums1),rob_helper(nums2))
        