class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]+1
        
        seq_stack=[nums[0]]
        start=1
        while start<len(nums) and nums[start]==seq_stack[-1]+1:
            seq_stack.append(nums[start])
            start+=1
        
        total_sum=sum(seq_stack)
        
        sort_seq=sorted(nums)
        
        for i in sort_seq:
            if total_sum==i:
                total_sum+=1
        
        return total_sum



        