class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        set_original=set(nums)
        start_points=[]
        
        for i in set_original:
            if i-1 not in set_original:
                start_points.append(i)

        seq=1
        for j in start_points:
            inc=0
            while j+inc in set_original:
                curr_len=inc+1
                inc+=1
            seq=max(seq,curr_len)
        
        return seq

        

        # if not nums:
        #     return 0
        # sort_nums=sorted(nums)

        # temp=1
        # fnl=temp
        # #print(sort_nums)

        # for i in range(1,len(sort_nums)):
        #     if sort_nums[i-1]==sort_nums[i]:
        #         pass
        #     elif sort_nums[i-1]+1==sort_nums[i]:
        #         temp+=1
        #     else:
        #         temp=1
        #     fnl=max(fnl,temp)

        #     #print("value of temp:",temp)
        #     #print("value of fnl:",fnl)
        
        # return fnl

             
        



        