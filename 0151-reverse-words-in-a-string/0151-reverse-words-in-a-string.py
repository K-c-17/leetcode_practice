class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        collector=s.strip().split(' ')
        collector.reverse()

        final=[x for x in collector if x!='']
        return ' '.join(final)
        