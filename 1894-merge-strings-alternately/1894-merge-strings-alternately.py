class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        holder=''
        for i in range(min(len(word1),len(word2))):
            holder+=word1[i]
            holder+=word2[i]
        holder+=word1[i+1:]
        holder+=word2[i+1:]
        return holder
        