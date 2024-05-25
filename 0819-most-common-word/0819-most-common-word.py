class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        collector={}
        new_para=''
        #pre-processing of the input paragraph
        for val in paragraph:
            if val in "!?',;.":
                new_para+=' '
            else:
                new_para+=lower(val)
        para_lower=[i for i in new_para.split(' ') if len(i)<>0 and i not in banned]
        print(para_lower)
        for i in set(para_lower):
                collector[i]=para_lower.count(i)
        #return max(collector.keys(),key=lambda x: collector[x])
        return max(collector.keys(),key=collector.get)
            

        