class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack=[]
        mapping={}
        for i in nums2:
            while stack and i>stack[-1]:
                element=stack.pop()
                mapping[element]=i
            stack.append(i)
        
        while stack:
            last=stack.pop()
            mapping[last]=-1
        
        print([mapping[x] for x in nums1])
        
        return [mapping[x] for x in nums1]


        