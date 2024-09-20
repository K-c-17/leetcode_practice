class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        collector={}
        #finding the frequency of every alphabet and storing this in a hash map
        for alphabet in s:
            if alphabet not in collector.keys():
                collector[alphabet]=1
            else:
                collector[alphabet]+=1
        
        #going over my input string and finding the first alphabet which is having a frequency of 1
        for i in range(len(s)):
            if collector[s[i]]==1:
                return i
        return -1