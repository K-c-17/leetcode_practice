class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1={}
        dict2={}
        for i in nums1:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        for j in nums2:
            if j in dict2:
                dict2[j]+=1
            else:
                dict2[j]=1
        
        min_dict={}
        for key,value in dict1.items():
            if key in dict2:
                min_dict[key]=min(dict1[key],dict2[key])
            else:
                pass

        return [key for key,value in min_dict.items() for _ in range(value)]


        
            

        