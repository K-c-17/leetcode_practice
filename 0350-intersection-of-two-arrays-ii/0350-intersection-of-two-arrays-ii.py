class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        combined=[nums1,nums2]
        collector=[]
        for lst in combined:
            def_dict=dict.fromkeys(range(0,1001),0)
            for num in lst:
                def_dict[num]+=1
            collector.append(def_dict)
        
        min_dict={}
        for val in collector:
            for i in val:
                if i not in min_dict or min_dict[i]>val[i]:
                    min_dict[i]=val[i]
                else:
                    pass
                    
        result=[]
        for key,value in min_dict.items():
            if value>0:
                result.extend([key]*value)
        return result


        
            

        