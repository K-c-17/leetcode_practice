class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        s1_freq,s2_freq=Counter(s1.split(" ")),Counter(s2.split(" "))

        final=[]
        #print(s1_freq,s2_freq)
        for i in s1_freq:
            if (s1_freq[i]==1 and i not in s2_freq):
                final.append(i)
        
        for j in s2_freq:
            if (s2_freq[j]==1 and j not in s1_freq):
                final.append(j)
        
        return final