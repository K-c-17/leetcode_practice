class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping=defaultdict(str)

        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            if s[i] in mapping.keys() and mapping[s[i]]!=t[i]:
                return False
            elif s[i] not in mapping.keys() and t[i] in set(mapping.values()):
                return False
            else:
                mapping[s[i]]=t[i]        
        return True

        
        