class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        total=0
        for i in words:
            if pref==i[:len(pref)]:
                total+=1
        return total
        