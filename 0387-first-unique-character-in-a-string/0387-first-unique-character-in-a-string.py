class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq=Counter(s)

        for i in range(len(s)):
            if freq[s[i]]==1:
                return i
        return -1