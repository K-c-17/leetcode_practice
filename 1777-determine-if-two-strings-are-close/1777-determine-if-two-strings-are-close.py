class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        freq1=Counter(word1)
        freq2=Counter(word2)
        
        if set(freq1.keys())!=set(freq2.keys()):
            return False
        
        elif sorted(freq1.values())!=sorted(freq2.values()):
            return False
        
        return True