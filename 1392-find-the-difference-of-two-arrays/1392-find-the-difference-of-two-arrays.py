class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set1={x for x in nums1}
        set2={y for y in nums2}

        part1=list(set1.difference(set2))
        part2=list(set2.difference(set1))

        return [part1,part2]
        