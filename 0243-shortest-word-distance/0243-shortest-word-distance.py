class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1Ind=[]
        word2Ind=[]
        dis=[]
        for i in range (0,len(wordsDict)):
            if wordsDict[i]==word1:
                word1Ind.append(i)
            elif wordsDict[i]==word2:
                word2Ind.append(i)
            if word1Ind and word2Ind:
                val=abs((word1Ind[-1])-(word2Ind[-1]))
                dis.append(val)
        return min(dis)

        