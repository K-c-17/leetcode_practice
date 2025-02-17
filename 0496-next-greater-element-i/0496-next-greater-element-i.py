class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        final=[]
        for i in nums1:
            start=nums2.index(i)
            exists=0
            for j in nums2[start+1:]:
                if j>i:
                    exists=1
                    final.append(j)
                    break
            if exists==0:
                final.append(-1)
        
        print(final)
        return final


        