class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        last=m+n-1


        while m>0 and n>0:
            if nums2[n-1]>nums1[m-1]:
                nums1[last]=nums2[n-1]
                n-=1
            else:
                nums1[last]=nums1[m-1]
                m-=1
            
            last-=1
        #adding the leftover of nums2 into nums1
        while n>0:
            nums1[last]=nums2[n-1]
            n-=1
            last-=1














        # temp=[0 for i in range(m+n)]

        # i,j,k=0,0,0

        # while i<m and j<n:
        #     if nums1[i]>nums2[j]:
        #         temp[k]=nums2[j]
        #         j+=1
        #         k+=1
        #     else:
        #         temp[k]=nums1[i]
        #         i+=1
        #         k+=1
        
        # #print(temp,i,j,k)
        # if i<m:
        #     temp[k:]=nums1[i:m]
        # elif j<n:
        #     temp[k:]=nums2[j:]
        
        # nums1[::1]=temp[::1]


        