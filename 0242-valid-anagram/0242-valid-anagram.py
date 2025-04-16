class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False

        s_map=collections.Counter(s)
        t_map=collections.Counter(t)

        return all(i in t_map and s_map[i]==t_map[i] for i in s_map.keys())
        