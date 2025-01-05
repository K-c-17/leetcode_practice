class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        freq1={}
        freq2={}
        for i in word1:
            if i not in freq1:
                freq1[i]=1
            else:
                freq1[i]+=1
        
        for j in word2:
            if j not in freq2:
                freq2[j]=1
            else:
                freq2[j]+=1
        
        sort_freq1=sorted([x for x in freq1.values()])
        sort_freq2=sorted([y for y in freq2.values()])

        if {x for x in freq1.keys()}.difference({y for y in freq2.keys()})!=set():
            return False
        elif sort_freq1!=sort_freq2:
            return False
        else:
            return True

        