class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        set_original=set(nums)
        temp=[]
        for i in set_original:
            if i-1 not in set_original:
                temp.append(i)
        #print(temp)
        seq=1
        for j in temp:
            cnt=1
            inc=0
            while j+inc in set_original:
                seq=max(seq,cnt+inc)
                inc+=1
                #print('For', j, 'iter value of seq is:', seq)
        
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

             
        



        