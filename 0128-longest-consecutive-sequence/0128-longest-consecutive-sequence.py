class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        sort_nums=sorted(nums)

        temp=1
        fnl=temp
        #print(sort_nums)

        for i in range(1,len(sort_nums)):
            if sort_nums[i-1]==sort_nums[i]:
                pass
            elif sort_nums[i-1]+1==sort_nums[i]:
                temp+=1
            else:
                temp=1
            fnl=max(fnl,temp)

            #print("value of temp:",temp)
            #print("value of fnl:",fnl)
        
        return fnl
             
        



        